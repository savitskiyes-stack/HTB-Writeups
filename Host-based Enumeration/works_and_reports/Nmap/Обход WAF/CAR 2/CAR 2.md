CAR 2





sudo nmap -sU -sV -p53 --script dns* 10.129.2.48

-sU: UDP-скан (отправляет UDP-запросы)

-p53: Только порт 53

--script dns*: Запускает все DNS-скрипты NSE

Если сервер на TCP-53 добавляем -sT





Starting Nmap 7.94SVN ( https://nmap.org ) at 2026-02-03 16:08 CST
Nmap scan report for 10.129.2.48
Host is up (0.044s latency).

PORT   STATE SERVICE VERSION
53/udp open  domain  (unknown banner: HTB{GoTtgUnyze9Psw4vGjcuMpHRp})
|_dns-cache-snoop: 0 of 100 tested domains are cached.
|_dns-nsec3-enum: Can't determine domain for host 10.129.2.48; use dns-nsec3-enum.domains script arg.
|_dns-fuzz: Server didn't response to our probe, can't fuzz
| dns-nsid: 
|_  bind.version: HTB{GoTtgUnyze9Psw4vGjcuMpHRp}
| fingerprint-strings: 
|   DNSVersionBindReq: 
|     version
|     bind
|     HTB{GoTtgUnyze9Psw4vGjcuMpHRp}
|   NBTStat: 
|     CKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
|_    ROOT-SERVERS
|_dns-nsec-enum: Can't determine domain for host 10.129.2.48; use dns-nsec-enum.domains script arg.
