Information gathering





#### Запрос:

#### Какая версия SMB-сервера установлена ​​на целевой системе? В качестве ответа отправьте весь баннер.

#### Ответ:

#### Samba smbd 4.6.2





Общий скан возможных портов для smb:





┌─\[eu-academy-3]─\[10.10.14.241]─\[htb-ac-2182889@htb-svbs9lbc8d]─\[~]

└──╼ \[★]$ namp -p 445 137 138 139 -sV -sC 10.129.27.158

bash: namp: command not found

┌─\[eu-academy-3]─\[10.10.14.241]─\[htb-ac-2182889@htb-svbs9lbc8d]─\[~]

└──╼ \[★]$ nmap -p 445 137 138 139 -sV -sC 10.129.27.158

Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-02-05 14:55 CST

Nmap scan report for 10.129.27.158

Host is up (0.051s latency).



PORT    STATE SERVICE     VERSION

445/tcp open  netbios-ssn Samba smbd 4.6.2



Host script results:

|\_clock-skew: -35s

| smb2-security-mode:

|   3:1:1:

|\_    Message signing enabled but not required

|\_nbstat: NetBIOS name: DEVSMB, NetBIOS user: <unknown>, NetBIOS MAC: <unknown> (unknown)

| smb2-time:

|   date: 2026-02-05T20:54:46

|\_  start\_date: N/A



Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 4 IP addresses (1 host up) scanned in 12.36 seconds

























#### Вопрос:

#### Как называется accessible share в целевой компании?

Ответ:
sambashare
---





┌─\[eu-academy-3]─\[10.10.14.241]─\[htb-ac-2182889@htb-svbs9lbc8d]─\[~]

└──╼ \[★]$ smbclient -N -L //10.129.27.158



&nbsp;	Sharename       Type      Comment

&nbsp;	---------       ----      -------

&nbsp;	print$          Disk      Printer Drivers

&nbsp;	sambashare      Disk      InFreight SMB v3.1

&nbsp;	IPC$            IPC       IPC Service (InlaneFreight SMB server (Samba, Ubuntu))

Reconnecting with SMB1 for workgroup listing.

smbXcli\_negprot\_smb1\_done: No compatible protocol selected by server.

protocol negotiation failed: NT\_STATUS\_INVALID\_NETWORK\_RESPONSE

Unable to connect with SMB1 -- no workgroup available















#### Вопрос:

#### Подключитесь к обнаруженной общей папке и найдите файл flag.txt. Отправьте его содержимое в качестве ответа.

Ответ:
falg.txt (содержимое файла скрыто по этическим соображениям)
---





Пароль admin



★]$ rpcclient -U "" 10.129.27.158

Password for \[WORKGROUP\\]:

rpcclient $> ls

command not found: ls

rpcclient $> srvinfo

&nbsp;	DEVSMB         Wk Sv PrQ Unx NT SNT InlaneFreight SMB server (Samba, Ubuntu)

&nbsp;	platform\_id     :	500

&nbsp;	os version      :	6.1

&nbsp;	server type     :	0x809a03

rpcclient $> enumdomains

name:\[DEVSMB] idx:\[0x0]

name:\[Builtin] idx:\[0x1]

rpcclient $> 









smb: \\> ls

&nbsp; .                                   D        0  Mon Nov  8 07:43:14 2021

&nbsp; ..                                  D        0  Mon Nov  8 09:53:19 2021

&nbsp; .profile                            H      807  Tue Feb 25 06:03:22 2020

&nbsp; contents                            D        0  Mon Nov  8 07:43:45 2021

&nbsp; .bash\_logout                        H      220  Tue Feb 25 06:03:22 2020

&nbsp; .bashrc                             H     3771  Tue Feb 25 06:03:22 2020



&nbsp;		4062912 blocks of size 1024. 414208 blocks available

smb: \\> cd contents

smb: \\contents\\> ls

&nbsp; .                                   D        0  Mon Nov  8 07:43:45 2021

&nbsp; ..                                  D        0  Mon Nov  8 07:43:14 2021

&nbsp; flag.txt                            N       38  Mon Nov  8 07:43:45 2021



&nbsp;		4062912 blocks of size 1024. 414204 blocks available

smb: \\contents\\> cat flag

cat: command not found

smb: \\contents\\> get flag.txt














Вопрос:
Выясните, к какому домену принадлежит сервер
---

Ответ:
DEVOPS


rpcclient $> querydominfo
---

Domain:		DEVOPS

Server:		DEVSMB

Comment:	InlaneFreight SMB server (Samba, Ubuntu)

Total Users:	0

Total Groups:	0

Total Aliases:	0

Sequence No:	1770328684

Force Logoff:	-1

Domain Server State:	0x1

Server Role:	ROLE\_DOMAIN\_PDC

Unknown 3:	0x1













#### Вопрос:

Найдите дополнительную информацию о accessible share, которую мы обнаружили ранее, и отправьте в качестве ответа модифицированную версию этой accessible share.
Ответ:
InFreight SMB v3.1
---







smbclient -N -L //10.129.27.158



&nbsp;	Sharename       Type      Comment

&nbsp;	---------       ----      -------

&nbsp;	print$          Disk      Printer Drivers

&nbsp;	sambashare      Disk      InFreight SMB v3.1

&nbsp;	IPC$            IPC       IPC Service (InlaneFreight SMB server (Samba, Ubuntu))











Вопрос:
---

#### Какой полный системный путь к этому accessible share? (формат: "/directory/names")

Ответ:
/home/sambauser
---





$ rpcclient -U "" 10.129.27.158 -c "netsharegetinfo sambashare"

Password for \[WORKGROUP\\]:

netname: sambashare

&nbsp;	remark:	InFreight SMB v3.1

&nbsp;	path:	C:\\home\\sambauser\\

&nbsp;	password:	

&nbsp;	type:	0x0

&nbsp;	perms:	0

&nbsp;	max\_uses:	-1

&nbsp;	num\_uses:	1

revision: 1

type: 0x8004: SEC\_DESC\_DACL\_PRESENT SEC\_DESC\_SELF\_RELATIVE 

DACL

&nbsp;	ACL	Num ACEs:	1	revision:	2

&nbsp;	---

&nbsp;	ACE

&nbsp;		type: ACCESS ALLOWED (0) flags: 0x00 

&nbsp;		Specific bits: 0x1ff

&nbsp;		Permissions: 0x1f01ff: SYNCHRONIZE\_ACCESS WRITE\_OWNER\_ACCESS WRITE\_DAC\_ACCESS READ\_CONTROL\_ACCESS DELETE\_ACCESS 

&nbsp;		SID: S-1-1-0






































