CAR 1

┌─[eu-academy-3]─[10.10.15.47]─[htb-ac-2182889@htb-c6bzyliugy]─[~]
└──╼ [★]$ sudo nmap -sV -Pn -n 10.129.23.205
Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-02-03 15:28 CST
Nmap scan report for 10.129.23.205
Host is up (0.051s latency).
Not shown: 869 closed tcp ports (reset), 128 filtered tcp ports (no-response)
PORT      STATE SERVICE     VERSION
22/tcp    open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http        Apache httpd 2.4.29 ((Ubuntu))
10001/tcp open  scp-config?
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port10001-TCP:V=7.94SVN%I=7%D=2/3%Time=698268A1%P=x86_64-pc-linux-gnu%r
SF:(GetRequest,1F,"220\x20HTB{pr0F7pDv3r510nb4nn3r}\r\n");
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 181.35 seconds










-sV        определяет версии сервисов на открытых портах

-Pn        не пингует хост перед сканированием

-n         не делает DNS-разрешения

Запускается от root (sudo)

-sS        из-за sudo стоит по умолчанию (стелс сканирование не завершает соединение и менее заметен в логах SYN-скан)

Больше стелса:
-T2 (замедление) или -D (decoys (RND:5 или 10))


