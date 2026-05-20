CAR 3





#### Скан портов:



sudo nmap -sV --script dns\* -Pn -n --source-port 53 10.129.23.245

Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-02-03 18:38 CST

Stats: 0:00:40 elapsed; 0 hosts completed (1 up), 1 undergoing Script Scan

NSE Timing: About 99.47% done; ETC: 18:39 (0:00:00 remaining)

Nmap scan report for 10.129.23.245

Host is up (0.051s latency).

Not shown: 848 closed tcp ports (reset), 149 filtered tcp ports (no-response)

PORT      STATE SERVICE    VERSION

22/tcp    open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.7 (Ubuntu Linux; protocol 2.0)

80/tcp    open  http       Apache httpd 2.4.29 ((Ubuntu))

50000/tcp open  tcpwrapped

|\_drda-info: TIMEOUT

Service Info: OS: Linux; CPE: cpe:/o:linux:linux\_kernel



Host script results:

| dns-blacklist: 

|   SPAM

|     l2.apews.org - FAIL

|     all.spamrats.com - FAIL

|\_    list.quorum.to - SPAM

|\_dns-brute: Can't guess domain of "10.129.23.245"; use dns-brute.domain script argument.



Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 62.76 seconds









Найден интересный порт  50000/tcp open  tcpwrapped











#### Скан порта:







─\[eu-academy-3]─\[10.10.15.47]─\[htb-ac-2182889@htb-hnaxolp2qv]─\[~]

└──╼ \[★]$ sudo nmap 10.129.23.245 -p50000 -sS -sV -Pn -n --disable-arp-ping --packet-trace --source-port 53

Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-02-03 18:54 CST

SENT (0.1024s) TCP 10.10.15.47:53 > 10.129.23.245:50000 S ttl=37 id=27090 iplen=44  seq=1117653351 win=1024 <mss 1460>

RCVD (0.1517s) TCP 10.129.23.245:50000 > 10.10.15.47:53 SA ttl=63 id=0 iplen=44  seq=4149775659 win=64240 <mss 1362>

NSOCK INFO \[0.2440s] nsock\_iod\_new2(): nsock\_iod\_new (IOD #1)

NSOCK INFO \[0.2450s] nsock\_connect\_tcp(): TCP connection requested to 10.129.23.245:50000 (IOD #1) EID 8

NSOCK INFO \[5.2500s] nsock\_trace\_handler\_callback(): Callback: CONNECT TIMEOUT for EID 8 \[10.129.23.245:50000]

NSOCK INFO \[5.2500s] nsock\_iod\_delete(): nsock\_iod\_delete (IOD #1)

NSOCK INFO \[5.2500s] nsock\_iod\_new2(): nsock\_iod\_new (IOD #1)

NSOCK INFO \[5.2510s] nsock\_connect\_tcp(): TCP connection requested to 10.129.23.245:50000 (IOD #1) EID 8

NSOCK INFO \[5.2510s] nsock\_iod\_new2(): nsock\_iod\_new (IOD #2)

NSOCK INFO \[5.2510s] nsock\_connect\_tcp(): TCP connection requested to 10.129.23.245:50000 (IOD #2) EID 16

NSOCK INFO \[6.2510s] nsock\_trace\_handler\_callback(): Callback: CONNECT TIMEOUT for EID 8 \[10.129.23.245:50000]

NSE: TCP 10.10.15.47:46806 > 10.129.23.245:50000 | CONNECT

NSE: TCP 10.10.15.47:46806 > 10.129.23.245:50000 | CLOSE

NSOCK INFO \[6.2600s] nsock\_iod\_delete(): nsock\_iod\_delete (IOD #1)

NSOCK INFO \[35.2510s] nsock\_trace\_handler\_callback(): Callback: CONNECT TIMEOUT for EID 16 \[10.129.23.245:50000]

NSE: TCP 10.10.15.47:46822 > 10.129.23.245:50000 | CONNECT

NSE: TCP 10.10.15.47:46822 > 10.129.23.245:50000 | CLOSE

NSOCK INFO \[35.2520s] nsock\_iod\_delete(): nsock\_iod\_delete (IOD #2)

Nmap scan report for 10.129.23.245

Host is up (0.049s latency).



PORT      STATE SERVICE    VERSION

50000/tcp open  tcpwrapped



Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .

Nmap done: 1 IP address (1 host up) scanned in 35.25 seconds





Попытка входа с NC



┌─\[eu-academy-3]─\[10.10.15.47]─\[htb-ac-2182889@htb-hnaxolp2qv]─\[~]
---

└──╼ \[★]$ sudo ncat -nv --source-port 53 10.129.23.245 50000

Ncat: Version 7.94SVN ( https://nmap.org/ncat )

Ncat: Connected to 10.129.23.245:50000.

220 HTB{kjnsdf2n982n1827eh76238s98di1w6}





















---

