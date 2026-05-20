#### FTP

#### 

#### 

#### получить инфо о настройках сервера:


ftp> status



Connected to 10.129.14.136.

No proxy connection.

Connecting using address family: any.

Mode: stream; Type: binary; Form: non-print; Structure: file

Verbose: on; Bell: off; Prompting: on; Globbing: on

Store unique: off; Receive unique: off

Case: off; CR stripping: on

Quote control characters: on

Ntrans: off

Nmap: off

Hash mark printing: off; Use of PORT cmds: on

Tick counter printing: off







Подробный вывод vsFTPd

---

ftp> debug



Debugging on (debug=1).





ftp> trace



Packet tracing on.





ftp> ls



---> PORT 10,10,14,4,188,195

200 PORT command successful. Consider using PASV.

---> LIST

150 Here comes the directory listing.

-rw-rw-r--    1 1002     1002      8138592 Sep 14 16:54 Calender.pptx

drwxrwxr-x    2 1002     1002         4096 Sep 14 17:03 Clients

drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Documents

drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Employees

-rw-rw-r--    1 1002     1002           41 Sep 14 16:45 Important Notes.txt

226 Directory send OK.





если эта hide\_ids=YESнастройка присутствует

представление UID и GUID сервиса будет перезаписано, что затруднит определение того, 

с какими правами были записаны и загружены эти файлы













Скрытие идентификационных данных - ДА





ftp> ls



---> TYPE A

200 Switching to ASCII mode.

ftp: setsockopt (ignored): Permission denied

---> PORT 10,10,14,4,223,101

200 PORT command successful. Consider using PASV.

---> LIST

150 Here comes the directory listing.

-rw-rw-r--    1 ftp     ftp      8138592 Sep 14 16:54 Calender.pptx

drwxrwxr-x    2 ftp     ftp         4096 Sep 14 17:03 Clients

drwxrwxr-x    2 ftp     ftp         4096 Sep 14 16:50 Documents

drwxrwxr-x    2 ftp     ftp         4096 Sep 14 16:50 Employees

-rw-rw-r--    1 ftp     ftp           41 Sep 14 16:45 Important Notes.txt

-rw-------    1 ftp     ftp            0 Sep 15 14:57 testupload.txt

226 Directory send OK.









Эта настройка является функцией безопасности, предотвращающей раскрытие локальных 

имен пользователей. Теоретически, используя имена пользователей атаковать 

такие сервисы, как FTP, SSH и многие другие, методом перебора паролей



на практике решения fail2ban теперь являются стандартной реализацией любой инфраструктуры, 

которая регистрирует IP-адрес и блокирует весь доступ к инфраструктуре после определенного 

количества неудачных попыток входа



(Юзаем прокси правда это может быть дорогое удовольствие ради лишь перебора)




полезная настройка:

ls\_recurse\_enable=YES

&nbsp;часто устанавливают на сервере vsFTPd для лучшего обзора 

структуры каталогов FTP, поскольку он позволяет одновременно 

видеть всё видимое содержимое




Рекурсивный листинг



ftp> ls -R



---> PORT 10,10,14,4,222,149

200 PORT command successful. Consider using PASV.

---> LIST -R

150 Here comes the directory listing.

.:

-rw-rw-r--    1 ftp      ftp      8138592 Sep 14 16:54 Calender.pptx

drwxrwxr-x    2 ftp      ftp         4096 Sep 14 17:03 Clients

drwxrwxr-x    2 ftp      ftp         4096 Sep 14 16:50 Documents

drwxrwxr-x    2 ftp      ftp         4096 Sep 14 16:50 Employees

-rw-rw-r--    1 ftp      ftp           41 Sep 14 16:45 Important Notes.txt

-rw-------    1 ftp      ftp            0 Sep 15 14:57 testupload.txt



./Clients:

drwx------    2 ftp      ftp          4096 Sep 16 18:04 HackTheBox

drwxrwxrwx    2 ftp      ftp          4096 Sep 16 18:00 Inlanefreight



./Clients/HackTheBox:

-rw-r--r--    1 ftp      ftp         34872 Sep 16 18:04 appointments.xlsx

-rw-r--r--    1 ftp      ftp        498123 Sep 16 18:04 contract.docx

-rw-r--r--    1 ftp      ftp        478237 Sep 16 18:04 contract.pdf

-rw-r--r--    1 ftp      ftp           348 Sep 16 18:04 meetings.txt



./Clients/Inlanefreight:

-rw-r--r--    1 ftp      ftp         14211 Sep 16 18:00 appointments.xlsx

-rw-r--r--    1 ftp      ftp         37882 Sep 16 17:58 contract.docx

-rw-r--r--    1 ftp      ftp            89 Sep 16 17:58 meetings.txt

-rw-r--r--    1 ftp      ftp        483293 Sep 16 17:59 proposal.pptx



./Documents:

-rw-r--r--    1 ftp      ftp         23211 Sep 16 18:05 appointments-template.xlsx

-rw-r--r--    1 ftp      ftp         32521 Sep 16 18:05 contract-template.docx

-rw-r--r--    1 ftp      ftp        453312 Sep 16 18:05 contract-template.pdf



./Employees:

226 Directory send OK.


Помимо файлов, можно просматривать, скачивать и анализировать их. 

Атаки также возможны с использованием FTP-журналов, что приводит к 

Remote Command Execution( RCE) это относится к FTP-сервисам и всем тем, 

которые можно обнаружить на этапе перечисления









Скачать файл:



ftp> ls



200 PORT command successful. Consider using PASV.

150 Here comes the directory listing.

-rwxrwxrwx    1 ftp      ftp             0 Sep 16 17:24 Calendar.pptx

drwxrwxrwx    4 ftp      ftp          4096 Sep 16 17:57 Clients

drwxrwxrwx    2 ftp      ftp          4096 Sep 16 18:05 Documents

drwxrwxrwx    2 ftp      ftp          4096 Sep 16 17:24 Employees

-rwxrwxrwx    1 ftp      ftp            41 Sep 18 15:58 Important Notes.txt

226 Directory send OK.





ftp> get Important\\ Notes.txt



local: Important Notes.txt remote: Important Notes.txt

200 PORT command successful. Consider using PASV.

150 Opening BINARY mode data connection for Important Notes.txt (41 bytes).

226 Transfer complete.

41 bytes received in 0.00 secs (606.6525 kB/s)





ftp> exit



221 Goodbye.








SavitskiyES@htb\[/htb]$ ls | grep Notes.txt



'Important Notes.txt'











также можно загрузить все доступные файлы и папки одновременно

(это может вызвать опасения, поскольку никто из сотрудников компании 

обычно не хочет загружать все файлы и контент сразу)





Скачать все доступные файлы:



SavitskiyES@htb\[/htb]$ wget -m --no-passive ftp://anonymous:anonymous@10.129.14.136



--2021-09-19 14:45:58--  ftp://anonymous:\*password\*@10.129.14.136/                                         

&nbsp;          => ‘10.129.14.136/.listing’                                                                     

Connecting to 10.129.14.136:21... connected.                                                               

Logging in as anonymous ... Logged in!

==> SYST ... done.    ==> PWD ... done.

==> TYPE I ... done.  ==> CWD not needed.

==> PORT ... done.    ==> LIST ... done.                                                                 

12.12.1.136/.listing           \[ <=>                                  ]     466  --.-KB/s    in 0s       

&nbsp;                                                                                                        

2021-09-19 14:45:58 (65,8 MB/s) - ‘10.129.14.136/.listing’ saved \[466]                                     

--2021-09-19 14:45:58--  ftp://anonymous:\*password\*@10.129.14.136/Calendar.pptx   

&nbsp;          => ‘10.129.14.136/Calendar.pptx’                                       

==> CWD not required.                                                           

==> SIZE Calendar.pptx ... done.                                                                                                                            

==> PORT ... done.    ==> RETR Calendar.pptx ... done.       



...SNIP...



2021-09-19 14:45:58 (48,3 MB/s) - ‘10.129.14.136/Employees/.listing’ saved \[119]



FINISHED --2021-09-19 14:45:58--

Total wall clock time: 0,03s

Downloaded: 15 files, 1,7K in 0,001s (3,02 MB/s)










Протокол FTP File Transfer Protocol(или FTPFTP) — один из старейших 

протоколов в интернете. FTP работает на прикладном уровне стека протоколов TCP/IP. 

Таким образом, он находится на том же уровне, что и HTTPдругие протоколы POP





Эти протоколы также работают с поддержкой браузеров или почтовых 

клиентов для предоставления своих услуг. Существуют также специальные 

FTP-программы для протокола передачи файлов





Список кодов состояния FTP https://en.wikipedia.org/wiki/List\_of\_FTP\_server\_return\_codes



Обычно для использования FTP на сервере требуются учетные данные. 

Также необходимо знать, что FTP — это clear-textпротокол, который 

иногда может быть перехвачен, если условия в сети благоприятны











После загрузки всех файлов мы wget создадим каталог с именем, соответствующим IP-адресу 

целевого объекта. Все загруженные файлы будут храниться там, и можно просмотреть их локально



SavitskiyES@htb\[/htb]$ tree .



.

└── 10.129.14.136

&nbsp;   ├── Calendar.pptx

&nbsp;   ├── Clients

&nbsp;   │   └── Inlanefreight

&nbsp;   │       ├── appointments.xlsx

&nbsp;   │       ├── contract.docx

&nbsp;   │       ├── meetings.txt

&nbsp;   │       └── proposal.pptx

&nbsp;   ├── Documents

&nbsp;   │   ├── appointments-template.xlsx

&nbsp;   │   ├── contract-template.docx

&nbsp;   │   └── contract-template.pdf

&nbsp;   ├── Employees

&nbsp;   └── Important Notes.txt



5 directories, 9 files




Возможность загружать файлы на FTP-сервер, подключенный к веб-серверу, увеличивает вероятность получения прямого доступа к веб-серверу и даже к обратной оболочке, которая позволяет выполнять внутренние системные команды и, возможно, даже повышать свои привилегии














проверка разрешения на загрузку файлов на FTP-сервер


SavitskiyES@htb\[/htb]$ touch testupload.txt


Загрузка на сервер:

---

ftp> put testupload.txt 



local: testupload.txt remote: testupload.txt

---> PORT 10,10,14,4,184,33

200 PORT command successful. Consider using PASV.

---> STOR testupload.txt

150 Ok to send data.

226 Transfer complete.





ftp> ls



---> TYPE A

200 Switching to ASCII mode.

---> PORT 10,10,14,4,223,101

200 PORT command successful. Consider using PASV.

---> LIST

150 Here comes the directory listing.

-rw-rw-r--    1 1002     1002      8138592 Sep 14 16:54 Calender.pptx

drwxrwxr-x    2 1002     1002         4096 Sep 14 17:03 Clients

drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Documents

drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Employees

-rw-rw-r--    1 1002     1002           41 Sep 14 16:45 Important Notes.txt

-rw-------    1 1002     133             0 Sep 15 14:57 testupload.txt

226 Directory send OK.







#### Доступ и безопасность:



Однако существует также возможность, что сервер предоставляет доступ к FTP anonymous FTP

В этом случае оператор сервера позволяет любому пользователю загружать или скачивать файлы через FTP без использования пароля. Поскольку с такими общедоступными FTP-серверами связаны риски безопасности, возможности пользователей обычно ограничены









TFTP

проще, чем FTP, и осуществляет передачу файлов между клиентским и серверным процессами

не обеспечивает аутентификацию пользователей и другие ценные функции, поддерживаемые FTP

FTP использует TCP, TFTP использует UDP UDP, что делает его ненадежным протоколом и заставляет 

его использовать восстановление на прикладном уровне с поддержкой UDP





TFTP в отличие от FTP, не требует аутентификации пользователя

Он не поддерживает защищенный вход по паролям и устанавливает 

ограничения на доступ, основываясь исключительно на правах чтения и 

записи файла в операционной системе







На практике TFTP работает исключительно в каталогах и с файлами, которые 

были предоставлены всем пользователям и могут читаться и записываться глобально

&nbsp;Из-за отсутствия безопасности TFTP, в отличие от FTP, может использоваться 

только в локальных и защищенных сетях

В отличие от FTP-клиента, TFTPне имеет 

функции отображения списка каталогов





Конфигурация по умолчанию

Одним из наиболее часто используемых FTP-серверов в дистрибутивах Linux является vsFTPd . 

Конфигурацию vsFTPd по умолчанию можно найти в файле `.config.js` /etc/vsftpd.conf, и 

некоторые параметры уже предопределены по умолчанию





/etc/ftpusers

он используется для запрета доступа к FTP-сервису определенным 

пользователям даже если они существуют в системе Linux



Дополнительные параметры , которые можно добавить в конфигурационный 

файл для анонимного входа, выглядят следующим образом:







+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| Параметр                     | Описание                                                                                                                                      |

+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| anonymous\_enable=YES         | Разрешить анонимный вход?                                                                                                                     |

| anon\_upload\_enable=YES       | Разрешить анонимным пользователям загружать файлы?                                                                                           |

| anon\_mkdir\_write\_enable=YES  | Разрешить анонимным пользователям создавать новые каталоги?                                                                                   |

| no\_anon\_password=YES         | Не запрашивать пароль у анонимных пользователей?                                                                                              |

| anon\_root=/home/username/ftp | Справочник для анонимных пользователей.                                                                                                       |

| write\_enable=YES             | Разрешить использование команд FTP: STOR, DELE, RNFR, RNTO, MKD, RMD, APPE и SITE?                                                            |

+------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+









С помощью стандартного FTP-клиента ( ftp) мы можем получить доступ к 

FTP-серверу и войти в систему под анонимным пользователем, если были 

использованы указанные выше настройки. Использование анонимной учетной 

записи может происходить во внутренних средах и инфраструктурах, где все 

участники известны. Доступ к этому типу сервиса может быть установлен 

временно или с помощью настройки для ускорения обмена файлами





Анонимный вход FTP

SavitskiyES@htb\[/htb]$ ftp 10.129.14.136



Connected to 10.129.14.136.

220 "Welcome to the HTB Academy vsFTP service."

Name (10.129.14.136:cry0l1t3): anonymous



230 Login successful.

Remote system type is UNIX.

Using binary mode to transfer files.





ftp> ls



200 PORT command successful. Consider using PASV.

150 Here comes the directory listing.

-rw-rw-r--    1 1002     1002      8138592 Sep 14 16:54 Calender.pptx

drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Clients

drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Documents

drwxrwxr-x    2 1002     1002         4096 Sep 14 16:50 Employees

-rw-rw-r--    1 1002     1002           41 Sep 14 16:45 Important Notes.txt

226 Directory send OK.















### Взаимодействие сервиса





FTP(NC)


SavitskiyES@htb\[/htb]$ nc -nv 10.129.14.136 21






FTP(telnet)



SavitskiyES@htb\[/htb]$ telnet 10.129.14.136 21













если FTP-сервер работает с шифрованием TLS/SSL

этом случае нужен клиент, способный обрабатывать TLS/SSL



Для этого мы можем использовать клиент openssl и взаимодействовать 

с FTP-сервером. Преимущество использования клиента opensslзаключается 

в том, что мы можем видеть SSL-сертификат, что также может быть полезно







SavitskiyES@htb\[/htb]$ openssl s\_client -connect 10.129.14.136:21 -starttls ftp



CONNECTED(00000003)                                                                                      

Can't use SSL\_get\_servername                        

depth=0 C = US, ST = California, L = Sacramento, O = Inlanefreight, OU = Dev, CN = master.inlanefreight.htb, emailAddress = admin@inlanefreight.htb

verify error:num=18:self signed certificate

verify return:1



depth=0 C = US, ST = California, L = Sacramento, O = Inlanefreight, OU = Dev, CN = master.inlanefreight.htb, emailAddress = admin@inlanefreight.htb

verify return:1

---                                                 

Certificate chain

&nbsp;0 s:C = US, ST = California, L = Sacramento, O = Inlanefreight, OU = Dev, CN = master.inlanefreight.htb, emailAddress = admin@inlanefreight.htb

&nbsp;

&nbsp;i:C = US, ST = California, L = Sacramento, O = Inlanefreight, OU = Dev, CN = master.inlanefreight.htb, emailAddress = admin@inlanefreight.htb

---

&nbsp;

Server certificate



-----BEGIN CERTIFICATE-----



MIIENTCCAx2gAwIBAgIUD+SlFZAWzX5yLs2q3ZcfdsRQqMYwDQYJKoZIhvcNAQEL

...SNIP...





SSL-сертификат позволяет нам распознавать hostname, например, и в большинстве случаев также идентификатор email addressорганизации или компании. Кроме того, если у компании несколько филиалов по всему миру, сертификаты могут быть созданы и для конкретных местоположений, которые также могут быть идентифицированы с помощью SSL-сертификата







































































































