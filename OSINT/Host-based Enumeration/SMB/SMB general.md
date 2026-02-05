##### SMB





клиент-серверный протокол, регулирующий доступ к файлам, целым каталогам и другим сетевым ресурсам, 

таким как принтеры, маршрутизаторы или интерфейсы, выделенные для сети

Обмен информацией между различными системными процессами также может 

осуществляться на основе протокола SMB



https://learn.microsoft.com/en-us/openspecs/windows\_protocols/ms-smb/f210069c-7086-4dc2-885e-861d837df688







##### Самба

альтернативная реализация SMB-сервера
разработанная для операционных систем на базе Unix. Samba реализует 

CIFSсетевой протокол Common Internet File System (CIFS)

специфическая реализация протокола SMB первоначально созданного Microsoft. 

Это позволяет Samba эффективно взаимодействовать с более новыми системами Windows 

Поэтому её часто называют SMB/CIFS

CIFS - считается специфической версией протокола SMB


 При передаче команд SMB через Samba в более старую службу NetBIOS 

соединения обычно устанавливаются через TCP-порты 137, 138, и 139. 

В отличие от этого, CIFS работает 445 исключительно через TCP-порт



+----------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| Версия SMB     | Поддерживается                    | Функции                                                                                                                                       |

+----------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| CIFS           | Windows NT 4.0                    | Связь осуществляется через интерфейс NetBIOS.                                                                                                 |

| SMB 1.0        | Windows 2000                      | Прямое соединение через TCP                                                                                                                   |

| SMB 2.0        | Windows Vista, Windows Server 2008 | Улучшена производительность, усовершенствована функция подписи сообщений, добавлено кэширование.                                              |

| SMB 2.1        | Windows 7, Windows Server 2008 R2 | Запирающие механизмы                                                                                                                          |

| SMB 3.0        | Windows 8, Windows Server 2012    | Многоканальные соединения, сквозное шифрование, удаленный доступ к хранилищу.                                                                 |

| SMB 3.0.2      | Windows 8.1, Windows Server 2012 R2 | -                                                                                                                                             |

| SMB 3.1.1      | Windows 10, Windows Server 2016   | Проверка целостности, шифрование AES-128                                                                                                      |

+----------------+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

---

#### 

#### 

#### 

#### 


Конфигурация по умолчанию


SavitskiyES@htb\[/htb]$ cat /etc/samba/smb.conf | grep -v "#\\|\\;" 
---



\[global]

&nbsp;  workgroup = DEV.INFREIGHT.HTB

&nbsp;  server string = DEVSMB

&nbsp;  log file = /var/log/samba/log.%m

&nbsp;  max log size = 1000

&nbsp;  logging = file

&nbsp;  panic action = /usr/share/samba/panic-action %d



&nbsp;  server role = standalone server

&nbsp;  obey pam restrictions = yes

&nbsp;  unix password sync = yes



&nbsp;  passwd program = /usr/bin/passwd %u

&nbsp;  passwd chat = \*Enter\\snew\\s\*\\spassword:\* %n\\n \*Retype\\snew\\s\*\\spassword:\* %n\\n \*password\\supdated\\ssuccessfully\* .



&nbsp;  pam password change = yes

&nbsp;  map to guest = bad user

&nbsp;  usershare allow guests = yes



\[printers]

&nbsp;  comment = All Printers

&nbsp;  browseable = no

&nbsp;  path = /var/spool/samba

&nbsp;  printable = yes

&nbsp;  guest ok = no

&nbsp;  read only = yes

&nbsp;  create mask = 0700



\[print$]

&nbsp;  comment = Printer Drivers

&nbsp;  path = /var/lib/samba/printers

&nbsp;  browseable = yes

&nbsp;  read only = yes

&nbsp;  guest ok = no











Настройки общих папок Samba (не полные)

Параметр	Описание
---

\[sharename]	Название сетевой папки.

workgroup = WORKGROUP/DOMAIN	Рабочая группа, которая будет отображаться при запросах клиентов.

path = /path/here/	Каталог, к которому пользователю будет предоставлен доступ.

server string = STRING	Строка, которая отобразится при установлении соединения.

unix password sync = yes	Синхронизировать пароль UNIX с паролем SMB?

usershare allow guests = yes	Разрешить неавторизованным пользователям доступ к определенной общей папке?

map to guest = bad user	Что делать, если запрос на вход пользователя не соответствует действующему пользователю UNIX?

browseable = yes	Следует ли отображать эту акцию в списке доступных акций?

guest ok = yes	Разрешить подключение к сервису без использования пароля?

read only = yes	Разрешить пользователям только чтение файлов?

create mask = 0700	Какие права доступа необходимо установить для вновь созданных файлов?





Опасные условия

Пример

Если 
browseable = yes

То как сотрудники так и получившие несанкционированный доступ могут также просматривать другие папки и файлы в них


---

###### 

###### 

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| Параметр                | Описание                                                                                                                                      |

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| browseable = yes        | Разрешить отображение списка доступных акций в текущей акции?                                                                                 |

| read only = no          | Запретить создание и изменение файлов?                                                                                                        |

| writable = yes          | Разрешить пользователям создавать и изменять файлы?                                                                                           |

| guest ok = yes          | Разрешить подключение к сервису без использования пароля?                                                                                     |

| enable privileges = yes | Привилегии чести, предоставленные конкретному SID?                                                                                            |

| create mask = 0777      | Какие права доступа необходимо назначить вновь созданным файлам?                                                                              |

| directory mask = 0777   | Какие права доступа необходимо назначить вновь созданным каталогам?                                                                           |

| logon script = script.sh | Какой скрипт необходимо выполнить при входе пользователя в систему?                                                                           |

| magic script = script.sh | Какой скрипт должен быть выполнен после закрытия скрипта?                                                                                     |

| magic output = script.out | Куда следует сохранять результаты работы магического скрипта?                                                                                  |

+-------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+



После настроек /etc/samba/smb.confк необходимо перезапустить службу на сервере
root@samba:~# sudo systemctl restart smbd



отобразить список ( -L) общих ресурсов сервера с помощью 

smbclient команды с нашего хоста.

используем так называемый null session( -N), который обеспечивает anonymous 

доступ без ввода существующих пользователей или действительных паролей











SMBclient — Подключение к общему ресурсу



SavitskiyES@htb\[/htb]$ smbclient -N -L //10.129.14.128



&nbsp;       Sharename       Type      Comment

&nbsp;       ---------       ----      -------

&nbsp;       print$          Disk      Printer Drivers

&nbsp;       home            Disk      INFREIGHT Samba

&nbsp;       dev             Disk      DEVenv

&nbsp;       notes           Disk      CheckIT

&nbsp;       IPC$            IPC       IPC Service (DEVSM)

SMB1 disabled -- no workgroup available









##### &nbsp;Smbclient позволяет выполнять локальные системные команды, используя 

##### восклицательный знак в начале ( !<cmd>), без прерывания соединения.


smb: \\> get prep-prod.txt 



getting file \\prep-prod.txt of size 71 as prep-prod.txt (8,7 KiloBytes/sec) 

(average 8,7 KiloBytes/sec)





smb: \\> !ls



prep-prod.txt





smb: \\> !cat prep-prod.txt



\[] check your code with the templates

\[] run code-assessment.py

\[] …	









smbstatus`samba install` 

Помимо версии Samba, мы также можем увидеть, кто, с какого 

хоста и к какой общей папке подключен клиент



root@samba:~# smbstatus



Samba version 4.11.6-Ubuntu

PID     Username     Group        Machine                                   Protocol Version  Encryption           Signing              

----------------------------------------------------------------------------------------------------------------------------------------

75691   sambauser    samba        10.10.14.4 (ipv4:10.10.14.4:45564)      SMB3\_11           -                    -                    



Service      pid     Machine       Connected at                     Encryption   Signing     

---------------------------------------------------------------------------------------------

notes        75691   10.10.14.4   Do Sep 23 00:12:06 2021 CEST     -            -           



No locked files















ЧЕКАЕМ ОБЩИЙ РЕСУР КОТОРЫЙ СОЗДАЛИ ДЛЯ ТЕСТА ПОСЛЕ НАСТРОЕК 

SavitskiyES@htb\[/htb]$ sudo nmap 10.129.14.128 -sV -sC -p139,445



Starting Nmap 7.80 ( https://nmap.org ) at 2021-09-19 15:15 CEST

Nmap scan report for sharing.inlanefreight.htb (10.129.14.128)

Host is up (0.00024s latency).



PORT    STATE SERVICE     VERSION

139/tcp open  netbios-ssn Samba smbd 4.6.2

445/tcp open  netbios-ssn Samba smbd 4.6.2

MAC Address: 00:00:00:00:00:00 (VMware)



Host script results:

|\_nbstat: NetBIOS name: HTB, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

| smb2-security-mode: 

|   2.02: 

|\_    Message signing enabled but not required

| smb2-time: 

|   date: 2021-09-19T13:16:04

|\_  start\_date: N/A



Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 11.35 seconds



















ИСИПОЛЬЗУЕМ ДРУГОЙ РЕСУР (Удаленный вызов процедур ( RPC RPC)):

SavitskiyES@htb\[/htb]$ rpcclient -U "" 10.129.14.128



Enter WORKGROUP\\'s password:

rpcclient $> 


+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| Запрос          | Описание                                                                                                                                      |

+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| srvinfo         | Информация о сервере.                                                                                                                         |

| enumdomains     | Перечислите все домены, развернутые в сети.                                                                                                   |

| querydominfo    | Предоставляет информацию о домене, сервере и пользователе развернутых доменов.                                                                |

| netshareenumall | Перечисляет все доступные акции.                                                                                                              |

| netsharegetinfo <share> | Предоставляет информацию о конкретной акции.                                                                                                  |

| enumdomusers    | Перечисляет всех пользователей домена.                                                                                                        |

| queryuser <RID> | Предоставляет информацию о конкретном пользователе.                                                                                           |

+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+




RPCclient - перечисление


rpcclient $> srvinfo



&nbsp;       DEVSMB         Wk Sv PrQ Unx NT SNT DEVSM

&nbsp;       platform\_id     :       500

&nbsp;       os version      :       6.1

&nbsp;       server type     :       0x809a03

&nbsp;		

&nbsp;		

rpcclient $> enumdomains



name:\[DEVSMB] idx:\[0x0]

name:\[Builtin] idx:\[0x1]





rpcclient $> querydominfo



Domain:         DEVOPS

Server:         DEVSMB

Comment:        DEVSM

Total Users:    2

Total Groups:   0

Total Aliases:  0

Sequence No:    1632361158

Force Logoff:   -1

Domain Server State:    0x1

Server Role:    ROLE\_DOMAIN\_PDC

Unknown 3:      0x1





rpcclient $> netshareenumall



netname: print$

&nbsp;       remark: Printer Drivers

&nbsp;       path:   C:\\var\\lib\\samba\\printers

&nbsp;       password:

netname: home

&nbsp;       remark: INFREIGHT Samba

&nbsp;       path:   C:\\home\\

&nbsp;       password:

netname: dev

&nbsp;       remark: DEVenv

&nbsp;       path:   C:\\home\\sambauser\\dev\\

&nbsp;       password:

netname: notes

&nbsp;       remark: CheckIT

&nbsp;       path:   C:\\mnt\\notes\\

&nbsp;       password:

netname: IPC$

&nbsp;       remark: IPC Service (DEVSM)

&nbsp;       path:   C:\\tmp

&nbsp;       password:

&nbsp;		

&nbsp;		

rpcclient $> netsharegetinfo notes



netname: notes

&nbsp;       remark: CheckIT

&nbsp;       path:   C:\\mnt\\notes\\

&nbsp;       password:

&nbsp;       type:   0x0

&nbsp;       perms:  0

&nbsp;       max\_uses:       -1

&nbsp;       num\_uses:       1

revision: 1

type: 0x8004: SEC\_DESC\_DACL\_PRESENT SEC\_DESC\_SELF\_RELATIVE 

DACL

&nbsp;       ACL     Num ACEs:       1       revision:       2

&nbsp;       ---

&nbsp;       ACE

&nbsp;               type: ACCESS ALLOWED (0) flags: 0x00 

&nbsp;               Specific bits: 0x1ff

&nbsp;               Permissions: 0x101f01ff: Generic all access SYNCHRONIZE\_ACCESS WRITE\_OWNER\_ACCESS WRITE\_DAC\_ACCESS READ\_CONTROL\_ACCESS DELETE\_ACCESS 

&nbsp;               SID: S-1-1-0















перечислить пользователей, используя rpcclient

---

rpcclient $> enumdomusers



user:\[mrb3n] rid:\[0x3e8]

user:\[cry0l1t3] rid:\[0x3e9]





rpcclient $> queryuser 0x3e9



&nbsp;       User Name   :   cry0l1t3

&nbsp;       Full Name   :   cry0l1t3

&nbsp;       Home Drive  :   \\\\devsmb\\cry0l1t3

&nbsp;       Dir Drive   :

&nbsp;       Profile Path:   \\\\devsmb\\cry0l1t3\\profile

&nbsp;       Logon Script:

&nbsp;       Description :

&nbsp;       Workstations:

&nbsp;       Comment     :

&nbsp;       Remote Dial :

&nbsp;       Logon Time               :      Do, 01 Jan 1970 01:00:00 CET

&nbsp;       Logoff Time              :      Mi, 06 Feb 2036 16:06:39 CET

&nbsp;       Kickoff Time             :      Mi, 06 Feb 2036 16:06:39 CET

&nbsp;       Password last set Time   :      Mi, 22 Sep 2021 17:50:56 CEST

&nbsp;       Password can change Time :      Mi, 22 Sep 2021 17:50:56 CEST

&nbsp;       Password must change Time:      Do, 14 Sep 30828 04:48:05 CEST

&nbsp;       unknown\_2\[0..31]...

&nbsp;       user\_rid :      0x3e9

&nbsp;       group\_rid:      0x201

&nbsp;       acb\_info :      0x00000014

&nbsp;       fields\_present: 0x00ffffff

&nbsp;       logon\_divs:     168

&nbsp;       bad\_password\_count:     0x00000000

&nbsp;       logon\_count:    0x00000000

&nbsp;       padding1\[0..7]...

&nbsp;       logon\_hrs\[0..21]...





rpcclient $> queryuser 0x3e8



&nbsp;       User Name   :   mrb3n

&nbsp;       Full Name   :

&nbsp;       Home Drive  :   \\\\devsmb\\mrb3n

&nbsp;       Dir Drive   :

&nbsp;       Profile Path:   \\\\devsmb\\mrb3n\\profile

&nbsp;       Logon Script:

&nbsp;       Description :

&nbsp;       Workstations:

&nbsp;       Comment     :

&nbsp;       Remote Dial :

&nbsp;       Logon Time               :      Do, 01 Jan 1970 01:00:00 CET

&nbsp;       Logoff Time              :      Mi, 06 Feb 2036 16:06:39 CET

&nbsp;       Kickoff Time             :      Mi, 06 Feb 2036 16:06:39 CET

&nbsp;       Password last set Time   :      Mi, 22 Sep 2021 17:47:59 CEST

&nbsp;       Password can change Time :      Mi, 22 Sep 2021 17:47:59 CEST

&nbsp;       Password must change Time:      Do, 14 Sep 30828 04:48:05 CEST

&nbsp;       unknown\_2\[0..31]...

&nbsp;       user\_rid :      0x3e8

&nbsp;       group\_rid:      0x201

&nbsp;       acb\_info :      0x00000010

&nbsp;       fields\_present: 0x00ffffff

&nbsp;       logon\_divs:     168

&nbsp;       bad\_password\_count:     0x00000000

&nbsp;       logon\_count:    0x00000000

&nbsp;       padding1\[0..7]...

&nbsp;       logon\_hrs\[0..21]...

















##### можем использовать полученные результаты для определения RID группы, который, 

в свою очередь, позволит нам получить информацию обо всей группе


Rpcclient - Информация о группе
---





rpcclient $> querygroup 0x201



&nbsp;       Group Name:     None

&nbsp;       Description:    Ordinary Users

&nbsp;       Group Attribute:7

&nbsp;       Num Members:2












#### 

#### можем создать объект, For-loopв Bashкотором мы отправляем команду в 

#### службу с помощью rpcclient и фильтруем результаты



SavitskiyES@htb\[/htb]$ for i in $(seq 500 1100);do rpcclient -N -U "" 10.129.14.128 -c "queryuser 0x$(printf '%x\\n' $i)" | grep "User Name\\|user\_rid\\|group\_rid" \&\& echo "";done



&nbsp;       User Name   :   sambauser

&nbsp;       user\_rid :      0x1f5

&nbsp;       group\_rid:      0x201

&nbsp;		

&nbsp;       User Name   :   mrb3n

&nbsp;       user\_rid :      0x3e8

&nbsp;       group\_rid:      0x201

&nbsp;		

&nbsp;       User Name   :   cry0l1t3

&nbsp;       user\_rid :      0x3e9

&nbsp;       group\_rid:      0x201













#### Подбор идентификаторов пользователей методом перебора



SavitskiyES@htb\[/htb]$ for i in $(seq 500 1100);do rpcclient -N -U "" 10.129.14.128 -c "queryuser 0x$(printf '%x\\n' $i)" | grep "User Name\\|user\_rid\\|group\_rid" \&\& echo "";done



&nbsp;       User Name   :   sambauser

&nbsp;       user\_rid :      0x1f5

&nbsp;       group\_rid:      0x201

&nbsp;		

&nbsp;       User Name   :   mrb3n

&nbsp;       user\_rid :      0x3e8

&nbsp;       group\_rid:      0x201

&nbsp;		

&nbsp;       User Name   :   cry0l1t3

&nbsp;       user\_rid :      0x3e9

&nbsp;       group\_rid:      0x201

















##### SMBmap





SavitskiyES@htb\[/htb]$ smbmap -H 10.129.14.128



\[+] Finding open SMB ports....

\[+] User SMB session established on 10.129.14.128...

\[+] IP: 10.129.14.128:445       Name: 10.129.14.128                                     

&nbsp;       Disk                                                    Permissions     Comment

&nbsp;       ----                                                    -----------     -------

&nbsp;       print$                                                  NO ACCESS       Printer Drivers

&nbsp;       home                                                    NO ACCESS       INFREIGHT Samba

&nbsp;       dev                                                     NO ACCESS       DEVenv

&nbsp;       notes                                                   NO ACCESS       CheckIT

&nbsp;       IPC$                                                    NO ACCESS       IPC Service (DEVSM)

















##### CrackMapExec





SavitskiyES@htb\[/htb]$ crackmapexec smb 10.129.14.128 --shares -u '' -p ''



SMB         10.129.14.128   445    DEVSMB           \[\*] Windows 6.1 Build 0 (name:DEVSMB) (domain:) (signing:False) (SMBv1:False)

SMB         10.129.14.128   445    DEVSMB           \[+] \\: 

SMB         10.129.14.128   445    DEVSMB           \[+] Enumerated shares

SMB         10.129.14.128   445    DEVSMB           Share           Permissions     Remark

SMB         10.129.14.128   445    DEVSMB           -----           -----------     ------

SMB         10.129.14.128   445    DEVSMB           print$                          Printer Drivers

SMB         10.129.14.128   445    DEVSMB           home                            INFREIGHT Samba

SMB         10.129.14.128   445    DEVSMB           dev                             DEVenv

SMB         10.129.14.128   445    DEVSMB           notes           READ,WRITE      CheckIT

SMB         10.129.14.128   445    DEVSMB           IPC$                            IPC Service (DEVSM)















#### Enum4Linux-ng



Установка Enum4Linux-ng



SavitskiyES@htb\[/htb]$ git clone https://github.com/cddmp/enum4linux-ng.git

SavitskiyES@htb\[/htb]$ cd enum4linux-ng

SavitskiyES@htb\[/htb]$ pip3 install -r requirements.txt









Enum4Linux-ng - Перечисление



SavitskiyES@htb\[/htb]$ ./enum4linux-ng.py 10.129.14.128 -A



ENUM4LINUX - next generation



&nbsp;==========================

|    Target Information    |

&nbsp;==========================

\[\*] Target ........... 10.129.14.128

\[\*] Username ......... ''

\[\*] Random Username .. 'juzgtcsu'

\[\*] Password ......... ''

\[\*] Timeout .......... 5 second(s)



&nbsp;=====================================

|    Service Scan on 10.129.14.128    |

&nbsp;=====================================

\[\*] Checking LDAP

\[-] Could not connect to LDAP on 389/tcp: connection refused

\[\*] Checking LDAPS

\[-] Could not connect to LDAPS on 636/tcp: connection refused

\[\*] Checking SMB

\[+] SMB is accessible on 445/tcp

\[\*] Checking SMB over NetBIOS

\[+] SMB over NetBIOS is accessible on 139/tcp



И ТД.

















































































































