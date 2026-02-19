Flags



Вопрос:
Взаимодействуйте с целевым DNS-сервером, используя его IP-адрес, и определите полное доменное имя (FQDN) для домена "inlanefreight.htb".


Решение:
dig any inlanefreight.htb @10.129.14.128


Ответ:
ns.inlanefreight.htb







Вопрос:
Определите, возможна ли передача зоны, и отправьте TXT-запись в качестве ответа. (Формат: HTB{...})

Решение:
Так как для основного домена axfr (полную передачу зоны) не позволяет я обратился к другому субдомену из выводу прошлой команды:


──╼ [★]$ dig axfr inlanefreight.htb @10.129.42.195

; <<>> DiG 9.18.33-1~deb12u2-Debian <<>> axfr inlanefreight.htb @10.129.42.195
;; global options: +cmd
inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
inlanefreight.htb.	604800	IN	TXT	"MS=ms97310371"
inlanefreight.htb.	604800	IN	TXT	"atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"
inlanefreight.htb.	604800	IN	TXT	"v=spf1 include:mailgun.org include:_spf.google.com include:spf.protection.outlook.com include:_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"
inlanefreight.htb.	604800	IN	NS	ns.inlanefreight.htb.
app.inlanefreight.htb.	604800	IN	A	10.129.18.15
dev.inlanefreight.htb.	604800	IN	A	10.12.0.1
internal.inlanefreight.htb. 604800 IN	A	10.129.1.6
mail1.inlanefreight.htb. 604800	IN	A	10.129.18.201
ns.inlanefreight.htb.	604800	IN	A	127.0.0.1
inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 49 msec
;; SERVER: 10.129.42.195#53(10.129.42.195) (TCP)
;; WHEN: Fri Feb 06 16:48:43 CST 2026
;; XFR size: 11 records (messages 1, bytes 560)


Получил:
└──╼ [★]$ dig axfr internal.inlanefreight.htb @10.129.42.195

; <<>> DiG 9.18.33-1~deb12u2-Debian <<>> axfr internal.inlanefreight.htb @10.129.42.195
;; global options: +cmd
internal.inlanefreight.htb. 604800 IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
internal.inlanefreight.htb. 604800 IN	TXT	"MS=ms97310371"
internal.inlanefreight.htb. 604800 IN	TXT	"HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}"
internal.inlanefreight.htb. 604800 IN	TXT	"atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"
internal.inlanefreight.htb. 604800 IN	TXT	"v=spf1 include:mailgun.org include:_spf.google.com include:spf.protection.outlook.com include:_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"
internal.inlanefreight.htb. 604800 IN	NS	ns.inlanefreight.htb.
dc1.internal.inlanefreight.htb.	604800 IN A	10.129.34.16
dc2.internal.inlanefreight.htb.	604800 IN A	10.129.34.11
mail1.internal.inlanefreight.htb. 604800 IN A	10.129.18.200
ns.internal.inlanefreight.htb. 604800 IN A	127.0.0.1
vpn.internal.inlanefreight.htb.	604800 IN A	10.129.1.6
ws1.internal.inlanefreight.htb.	604800 IN A	10.129.1.34
ws2.internal.inlanefreight.htb.	604800 IN A	10.129.1.35
wsus.internal.inlanefreight.htb. 604800	IN A	10.129.18.2
internal.inlanefreight.htb. 604800 IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800
;; Query time: 49 msec
;; SERVER: 10.129.42.195#53(10.129.42.195) (TCP)
;; WHEN: Fri Feb 06 17:00:08 CST 2026
;; XFR size: 15 records (messages 1, bytes 677)


Ответ:
"HTB{DN5_z0N3_7r4N5F3r_iskdufhcnlu34}"




Вопрос:
Какой IPv4-адрес у хоста DC1?

Ответ:
Из вывода команды выше мы видим что адрес:
dc1.internal.inlanefreight.htb.	604800 IN A	10.129.34.16








Вопрос:
Какое полное доменное имя (FQDN) у хоста, у которого последний октет заканчивается на "xxx203"?

Ответ:
в силу того что ни один из субдоменов не возвращал axfr пришлось брутфорсить по словарям:
dnsenum --dnsserver 10.129.14.128 --enum -p 0 -s 0 -o subdomains.txt -f /opt/useful/seclists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb



win2k.dev.inlanefreight.htb








