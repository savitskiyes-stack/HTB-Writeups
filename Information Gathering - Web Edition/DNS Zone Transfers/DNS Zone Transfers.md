DNS Zone Transfers



Что такое перенос зоны?

Перенос зоны DNS по сути представляет собой полную копию всех записей DNS в зоне (домена и его поддоменов) с одного сервера имен на другой. Этот процесс необходим для обеспечения согласованности и избыточности между серверами DNS. Однако, если он не защищен должным образом, неавторизованные лица могут загрузить весь файл зоны, получив полный список поддоменов, связанных с ними IP-адресов и других конфиденциальных данных DNS.











1 Zone Transfer Request (AXFR)Вторичный DNS-сервер инициирует процесс, отправляя запрос на передачу 

зоны на основной сервер. Этот запрос обычно использует тип AXFR (полная передача зоны).





2 SOA Record TransferПосле получения запроса (и, возможно, аутентификации вторичного сервера) основной 

сервер отвечает, отправляя запись начала полномочий (SOA). Запись SOA содержит важную информацию о зоне, 

включая ее серийный номер, что помогает вторичному серверу определить, актуальны ли данные зоны.





3 DNS Records TransmissionОсновной сервер затем поочередно передает все DNS-записи в зоне на резервный сервер. 

Это включает в себя записи типа A, AAAA, MX, CNAME, NS и другие, определяющие поддомены домена, почтовые серверы, 

серверы имен и другие конфигурации.





4 Zone Transfer CompleteПосле передачи всех записей основной сервер сигнализирует об окончании передачи зоны. 

Это уведомление информирует резервный сервер о том, что он получил полную копию данных зоны.





5 Acknowledgement (ACK)Вторичный сервер отправляет подтверждающее сообщение основному серверу, подтверждающее 

успешное получение и обработку данных зоны. На этом процесс передачи зоны завершается.



















Информация, полученная в результате несанкционированной передачи зоны, может оказаться бесценной для злоумышленника. 

Она раскрывает полную карту DNS-инфраструктуры цели, включая:





\- SubdomainsПолный список поддоменов, многие из которых могут не быть связаны ссылками с основным веб-сайтом 

или их может быть сложно обнаружить другими способами. На этих скрытых поддоменах могут размещаться серверы 

разработки, тестовые среды, административные панели или другие конфиденциальные ресурсы.





\- IP AddressesIP-адреса, связанные с каждым поддоменом, предоставляют потенциальные цели для дальнейшей разведки или атак.







\- Name Server RecordsПодробная информация об авторитетных серверах имен для домена, раскрывающая информацию о 

хостинг-провайдере и потенциальных ошибках конфигурации.











##### Для запроса переноса зоны:



SavitskiyES@htb\[/htb]$ dig axfr @nsztm1.digi.ninja zonetransfer.me

axfr (запрос который запрашивает полную копию зоны)







Если разрешено мы получим данные:

SavitskiyES@htb\[/htb]$ dig axfr @nsztm1.digi.ninja zonetransfer.me



; <<>> DiG 9.18.12-1~bpo11+1-Debian <<>> axfr @nsztm1.digi.ninja zonetransfer.me

; (1 server found)

;; global options: +cmd

zonetransfer.me.	7200	IN	SOA	nsztm1.digi.ninja. robin.digi.ninja. 2019100801 172800 900 1209600 3600

zonetransfer.me.	300	IN	HINFO	"Casio fx-700G" "Windows XP"

zonetransfer.me.	301	IN	TXT	"google-site-verification=tyP28J7JAUHA9fw2sHXMgcCC0I6XBmmoVi04VlMewxA"

zonetransfer.me.	7200	IN	MX	0 ASPMX.L.GOOGLE.COM.

...

zonetransfer.me.	7200	IN	A	5.196.105.14

zonetransfer.me.	7200	IN	NS	nsztm1.digi.ninja.

zonetransfer.me.	7200	IN	NS	nsztm2.digi.ninja.

\_acme-challenge.zonetransfer.me. 301 IN	TXT	"6Oa05hbUJ9xSsvYy7pApQvwCUSSGgxvrbdizjePEsZI"

\_sip.\_tcp.zonetransfer.me. 14000 IN	SRV	0 0 5060 www.zonetransfer.me.

14.105.196.5.IN-ADDR.ARPA.zonetransfer.me. 7200	IN PTR www.zonetransfer.me.

asfdbauthdns.zonetransfer.me. 7900 IN	AFSDB	1 asfdbbox.zonetransfer.me.

asfdbbox.zonetransfer.me. 7200	IN	A	127.0.0.1

asfdbvolume.zonetransfer.me. 7800 IN	AFSDB	1 asfdbbox.zonetransfer.me.

canberra-office.zonetransfer.me. 7200 IN A	202.14.81.230

...

;; Query time: 10 msec

;; SERVER: 81.4.108.41#53(nsztm1.digi.ninja) (TCP)

;; WHEN: Mon May 27 18:31:35 BST 2024

;; XFR size: 50 records (messages 1, bytes 2085)





где zonetransfer.me это сервис, специально созданный для демонстрации рисков передачи зон, чтобы dig команда возвращала полную запись зоны.













Запрашиваем копию зоны (где ip=целевой inlanefreight.htb=доменное имя основного хоста)



┌─\[eu-academy-3]─\[10.10.15.99]─\[htb-ac-2182889@htb-kex2aimet5]─\[~]

└──╼ \[★]$ dig axfr @10.129.42.195 inlanefreight.htb



; <<>> DiG 9.18.33-1~deb12u2-Debian <<>> axfr @10.129.42.195 inlanefreight.htb

; (1 server found)

;; global options: +cmd

inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800

inlanefreight.htb.	604800	IN	NS	ns.inlanefreight.htb.

admin.inlanefreight.htb. 604800	IN	A	10.10.34.2

ftp.admin.inlanefreight.htb. 604800 IN	A	10.10.34.2

careers.inlanefreight.htb. 604800 IN	A	10.10.34.50

dc1.inlanefreight.htb.	604800	IN	A	10.10.34.16

dc2.inlanefreight.htb.	604800	IN	A	10.10.34.11

internal.inlanefreight.htb. 604800 IN	A	127.0.0.1

admin.internal.inlanefreight.htb. 604800 IN A	10.10.1.11

wsus.internal.inlanefreight.htb. 604800	IN A	10.10.1.240

ir.inlanefreight.htb.	604800	IN	A	10.10.45.5

dev.ir.inlanefreight.htb. 604800 IN	A	10.10.45.6

ns.inlanefreight.htb.	604800	IN	A	127.0.0.1

resources.inlanefreight.htb. 604800 IN	A	10.10.34.100

securemessaging.inlanefreight.htb. 604800 IN A	10.10.34.52

test1.inlanefreight.htb. 604800	IN	A	10.10.34.101

us.inlanefreight.htb.	604800	IN	A	10.10.200.5

cluster14.us.inlanefreight.htb.	604800 IN A	10.10.200.14

messagecenter.us.inlanefreight.htb. 604800 IN A	10.10.200.10

ww02.inlanefreight.htb.	604800	IN	A	10.10.34.112

www1.inlanefreight.htb.	604800	IN	A	10.10.34.111

inlanefreight.htb.	604800	IN	SOA	inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800

;; Query time: 46 msec

;; SERVER: 10.129.42.195#53(10.129.42.195) (TCP)

;; WHEN: Wed Mar 04 07:47:07 CST 2026

;; XFR size: 22 records (messages 1, bytes 594)















































