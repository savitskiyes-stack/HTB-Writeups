DNS







Существует несколько типов DNS-серверов, используемых по всему миру:



Корневой DNS-сервер

Авторитетный сервер имен

Неавторитетный сервер имен

Кэширующий сервер

Сервер переадресации

Резолвер







+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| Тип сервера                 | Описание                                                                                                                                      |

+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| DNS Root Server             | Корневые серверы DNS отвечают за домены верхнего уровня ( TLD). Они запрашиваются только в том случае, если сервер имен не отвечает. Таким образом, корневой сервер является центральным интерфейсом между пользователями и контентом в Интернете, поскольку он связывает домен и IP-адрес. Корпорация по присвоению имен и номеров в Интернете ( ICANNIDN) координирует работу корневых серверов имен. 13Такие корневые серверы расположены по всему миру. |

| Authoritative Nameserver    | Авторитетные серверы имен обладают полномочиями для определенной зоны. Они отвечают только на запросы из своей зоны ответственности, и их информация является обязательной. Если авторитетный сервер имен не может ответить на запрос клиента, управление переходит к корневому серверу имен. В зависимости от страны, компании и т. д., авторитетные серверы имен предоставляют ответы рекурсивным DNS-серверам, помогая найти конкретный веб-сервер (серверы). |

| Non-authoritative Nameserver | Неавторитетные серверы имен не отвечают за конкретную DNS-зону. Вместо этого они самостоятельно собирают информацию о конкретных DNS-зонах, используя рекурсивные или итеративные DNS-запросы. |

| Caching DNS Server          | DNS-серверы, осуществляющие кэширование, кэшируют информацию от других серверов имен на определенный период времени. Продолжительность этого хранения определяет авторитетный сервер имен. |

| Forwarding Server           | Серверы переадресации выполняют только одну функцию: они пересылают DNS-запросы на другой DNS-сервер. |

| Resolver                    | Резолверы не являются авторитетными DNS-серверами, а выполняют разрешение имен локально на компьютере или маршрутизаторе. |

+-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+









DNS в основном не зашифрован



устройства в локальной сети WLAN и интернет-провайдеры могут 

взламывать систему и перехватывать DNS-запросы

&nbsp;в настоящее время существуют решения для шифрования DNS

По умолчанию специалисты по информационной безопасности 

применяют здесь DNS over TLS( DoT) или DNS over HTTPS( DoH). 

Кроме того, сетевой протокол DNSCryptтакже шифрует трафик 

между компьютером и сервером имен











DNS  также хранит и выдает дополнительную информацию о службах, связанных с доменом

DNS-запрос можно использовать, например, для определения того, какой компьютер служит 

почтовым сервером для данного домена или как называются серверы имен домена





+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| DNS-запись        | Описание                                                                                                                                      |

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| A                 | В результате возвращает IPv4-адрес запрошенного домена.                                                                                         |

| AAAA              | Возвращает IPv6-адрес запрошенного домена.                                                                                                    |

| MX                | В результате возвращаются ответственные почтовые серверы.                                                                                       |

| NS                | Возвращает DNS-серверы (серверы имен) домена.                                                                                                 |

| TXT               | Эта запись может содержать различную информацию. Универсальный инструмент может использоваться, например, для проверки Google Search Console или проверки SSL-сертификатов. Кроме того, задаются записи SPF и DMARC для проверки почтового трафика и защиты его от спама. |

| CNAME             | Эта запись служит псевдонимом для другого доменного имени. Если вы хотите, чтобы домен www.hackthebox.eu указывал на тот же IP-адрес, что и hackthebox.eu, вам нужно создать запись A для hackthebox.eu и запись CNAME для www.hackthebox.eu. |

| PTR               | Запись PTR работает в обратном направлении (обратный поиск). Она преобразует IP-адреса в действительные доменные имена.                       |

| SOA               | Предоставляет информацию о соответствующей DNS-зоне и адресе электронной почты административного контакта.                                     |

+-------------------+-----------------------------------------------------------------------------------------------------------------------------------------------+













SOA запись находится в файле зоны домена и определяет, кто отвечает 

за работу домена и как управляется информация DNS для этого домена

Точка (.) в адресе электронной почты заменяется знаком «@». 

В этом примере адрес электронной почты администратора — awsdns-hostmaster@amazon.com





SavitskiyES@htb\[/htb]$ dig soa www.inlanefreight.com



; <<>> DiG 9.16.27-Debian <<>> soa www.inlanefreight.com

;; global options: +cmd

;; Got answer:

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15876

;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1



;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 512

;; QUESTION SECTION:

;www.inlanefreight.com.         IN      SOA



;; AUTHORITY SECTION:

inlanefreight.com.      900     IN      SOA     ns-161.awsdns-20.com. awsdns-hostmaster.amazon.com. 1 7200 900 1209600 86400



;; Query time: 16 msec

;; SERVER: 8.8.8.8#53(8.8.8.8)

;; WHEN: Thu Jan 05 12:56:10 GMT 2023

;; MSG SIZE  rcvd: 128









##### Конфигурация по умолчанию:



локальные файлы конфигурации DNS

файлы зон

файлы обратного разрешения имен







DNS-сервер Bind9 очень часто используется в дистрибутивах на базе Linux. 

Его локальный конфигурационный файл ( named.conf) условно разделен на 

две части: во-первых, раздел параметров для общих настроек, 

и во-вторых, записи зон для отдельных доменов







#### Локальные конфигурационные файлы 

#### обычно выглядят следующим образом:



named.conf.local

named.conf.options

named.conf.log





named.conf разделен на несколько параметров, 

которые управляют поведением сервера имен. 

Различают параметры global options и zone options

Глобальные параметры являются общими и влияют на все зоны. 

Параметр зоны влияет только на ту зону, к которой он назначен. 

Параметры, не указанные в named.conf, имеют значения по умолчанию. 

Если параметр является одновременно глобальным и специфичным 

для зоны, то приоритет имеет параметр зоны











###### Локальная настройка DNS

&nbsp; 

root@bind9:~# cat /etc/bind/named.conf.local



//

// Do any local configuration here

//



// Consider adding the 1918 zones here, if they are not used in your

// organization

//include "/etc/bind/zones.rfc1918";

zone "domain.com" {

&nbsp;   type master;

&nbsp;   file "/etc/bind/db.domain.com";

&nbsp;   allow-update { key rndc-key; };

};











все данные forward records вводятся в соответствии с форматом BIND. 

Это позволяет DNS-серверу определить, к какому домену, имени хоста 

и роли относятся IP-адреса. Проще говоря, это телефонная книга, 

где DNS-сервер ищет адреса для доменов, которые он ищет







Файлы зон



root@bind9:~# cat /etc/bind/db.domain.com



;

; BIND reverse data file for local loopback interface

;

$ORIGIN domain.com

$TTL 86400

@     IN     SOA    dns1.domain.com.     hostmaster.domain.com. (

&nbsp;                   2001062501 ; serial

&nbsp;                   21600      ; refresh after 6 hours

&nbsp;                   3600       ; retry after 1 hour

&nbsp;                   604800     ; expire after 1 week

&nbsp;                   86400 )    ; minimum TTL of 1 day



&nbsp;     IN     NS     ns1.domain.com.

&nbsp;     IN     NS     ns2.domain.com.



&nbsp;     IN     MX     10     mx.domain.com.

&nbsp;     IN     MX     20     mx2.domain.com.



&nbsp;            IN     A       10.129.14.5



server1      IN     A       10.129.14.5

server2      IN     A       10.129.14.7

ns1          IN     A       10.129.14.2

ns2          IN     A       10.129.14.3



ftp          IN     CNAME   server1

mx           IN     CNAME   server1

mx2          IN     CNAME   server2

www          IN     CNAME   server2











###### Для того чтобы имя компьютера Fully Qualified Domain Name( FQDN) 

###### было разрешено из IP-адреса, DNS-сервер должен иметь файл обратного поиска











###### Файлы зон обратного разрешения имен

root@bind9:~# cat /etc/bind/db.10.129.14



;

; BIND reverse data file for local loopback interface

;

$ORIGIN 14.129.10.in-addr.arpa

$TTL 86400

@     IN     SOA    dns1.domain.com.     hostmaster.domain.com. (

&nbsp;                   2001062501 ; serial

&nbsp;                   21600      ; refresh after 6 hours

&nbsp;                   3600       ; retry after 1 hour

&nbsp;                   604800     ; expire after 1 week

&nbsp;                   86400 )    ; minimum TTL of 1 day



&nbsp;     IN     NS     ns1.domain.com.

&nbsp;     IN     NS     ns2.domain.com.



5    IN     PTR    server1.domain.com.

7    IN     MX     mx.domain.com.

...SNIP...









###### 

###### Опасные условия



краткий список наиболее распространенных атак на DNS-серверы

https://web.archive.org/web/20250329174745/https://securitytrails.com/blog/most-popular-types-dns-attacks









Некоторые из настроек, которые мы видим ниже, 

приводят к этим и другим уязвимостям



+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| Вариант        | Описание                                                                                                                                      |

+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| allow-query    | Определяет, каким хостам разрешено отправлять запросы на DNS-сервер.                                                                         |

| allow-recursion | Определяет, каким хостам разрешено отправлять рекурсивные запросы к DNS-серверу.                                                             |

| allow-transfer | Определяет, каким хостам разрешено получать данные о передаче зон от DNS-сервера.                                                             |

| zone-statistics | Собирает статистические данные по зонам.                                                                                                      |

+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+





















##### Создание базы данных для сервиса



DIG - NS Query



SavitskiyES@htb\[/htb]$ dig ns inlanefreight.htb @10.129.14.128



; <<>> DiG 9.16.1-Ubuntu <<>> ns inlanefreight.htb @10.129.14.128

;; global options: +cmd

;; Got answer:

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 45010

;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 2



;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 4096

; COOKIE: ce4d8681b32abaea0100000061475f73842c401c391690c7 (good)

;; QUESTION SECTION:

;inlanefreight.htb.             IN      NS



;; ANSWER SECTION:

inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.



;; ADDITIONAL SECTION:

ns.inlanefreight.htb.   604800  IN      A       10.129.34.136



;; Query time: 0 msec

;; SERVER: 10.129.14.128#53(10.129.14.128)

;; WHEN: So Sep 19 18:04:03 CEST 2021

;; MSG SIZE  rcvd: 107













Иногда также можно запросить версию DNS-сервера, 

используя запрос класса CHAOS и тип TXT. Однако 

эта запись должна существовать на DNS-сервере. 

Для этого можно использовать следующую команду:





DIG - Запрос версии



SavitskiyES@htb\[/htb]$ dig CH TXT version.bind 10.129.120.85



; <<>> DiG 9.10.6 <<>> CH TXT version.bind

;; global options: +cmd

;; Got answer:

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 47786

;; flags: qr aa rd; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1



;; ANSWER SECTION:

version.bind.       0       CH      TXT     "9.10.6-P1"



;; ADDITIONAL SECTION:

version.bind.       0       CH      TXT     "9.10.6-P1-Debian"



;; Query time: 2 msec

;; SERVER: 10.129.120.85#53(10.129.120.85)

;; WHEN: Wed Jan 05 20:23:14 UTC 2023

;; MSG SIZE  rcvd: 101



















###### ANY просмотра всех доступных записей

###### Это заставит сервер показать нам все 

###### доступные записи, которые он готов 

###### предоставить. 

###### 

###### Важно!!! что будут показаны не все записи из зон











DIG - ЛЮБОЙ запрос



SavitskiyES@htb\[/htb]$ dig any inlanefreight.htb @10.129.14.128



; <<>> DiG 9.16.1-Ubuntu <<>> any inlanefreight.htb @10.129.14.128

;; global options: +cmd

;; Got answer:

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 7649

;; flags: qr aa rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 2



;; OPT PSEUDOSECTION:

; EDNS: version: 0, flags:; udp: 4096

; COOKIE: 064b7e1f091b95120100000061476865a6026d01f87d10ca (good)

;; QUESTION SECTION:

;inlanefreight.htb.             IN      ANY



;; ANSWER SECTION:

inlanefreight.htb.      604800  IN      TXT     "v=spf1 include:mailgun.org include:\_spf.google.com include:spf.protection.outlook.com include:\_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"

inlanefreight.htb.      604800  IN      TXT     "atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"

inlanefreight.htb.      604800  IN      TXT     "MS=ms97310371"

inlanefreight.htb.      604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800

inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.



;; ADDITIONAL SECTION:

ns.inlanefreight.htb.   604800  IN      A       10.129.34.136



;; Query time: 0 msec

;; SERVER: 10.129.14.128#53(10.129.14.128)

;; WHEN: So Sep 19 18:42:13 CEST 2021

;; MSG SIZE  rcvd: 437













Синхронизация между задействованными серверами осуществляется 

посредством передачи зоны. Используя секретный ключ rndc-key, 

который мы рассматривали в начале конфигурации по умолчанию, 

серверы обеспечивают связь со своим собственным мастером или ведомым сервером





Для некоторых Top-Level Domains( TLDs) обеспечение Second Level Domainsдоступности 

файлов зоны как минимум на двух серверах является обязательным













##### DNS-сервер, который служит прямым источником для синхронизации файла зоны, называется основным сервером (master)



##### DNS-сервер, который получает данные зоны от основного сервера, называется подчиненным сервером (slave).








 Если порядковый номер записи SOA ведущего модуля больше, чем у подчиненного, наборы данных перестают совпадать.

SavitskiyES@htb\[/htb]$ dig axfr inlanefreight.htb @10.129.14.128



; <<>> DiG 9.16.1-Ubuntu <<>> axfr inlanefreight.htb @10.129.14.128

;; global options: +cmd

inlanefreight.htb.      604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800

inlanefreight.htb.      604800  IN      TXT     "MS=ms97310371"

inlanefreight.htb.      604800  IN      TXT     "atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"

inlanefreight.htb.      604800  IN      TXT     "v=spf1 include:mailgun.org include:\_spf.google.com include:spf.protection.outlook.com include:\_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"

inlanefreight.htb.      604800  IN      NS      ns.inlanefreight.htb.

app.inlanefreight.htb.  604800  IN      A       10.129.18.15

internal.inlanefreight.htb. 604800 IN   A       10.129.1.6

mail1.inlanefreight.htb. 604800 IN      A       10.129.18.201

ns.inlanefreight.htb.   604800  IN      A       10.129.34.136

inlanefreight.htb.      604800  IN      SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800

;; Query time: 4 msec

;; SERVER: 10.129.14.128#53(10.129.14.128)

;; WHEN: So Sep 19 18:51:19 CEST 2021

;; XFR size: 9 records (messages 1, bytes 520)





Если администратор использовал подсеть в качестве allow-transferопции 

для тестирования или в качестве обходного решения, или установил её 

значение на any, то все будут запрашивать весь файл зоны на DNS-сервере. 

Кроме того, могут быть запрошены другие зоны, которые могут даже отображать 

внутренние IP-адреса и имена хостов







###### DIG - AXFR Zone Transfer - Internal



SavitskiyES@htb\[/htb]$ dig axfr internal.inlanefreight.htb @10.129.14.128



; <<>> DiG 9.16.1-Ubuntu <<>> axfr internal.inlanefreight.htb @10.129.14.128

;; global options: +cmd

internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800

internal.inlanefreight.htb. 604800 IN   TXT     "MS=ms97310371"

internal.inlanefreight.htb. 604800 IN   TXT     "atlassian-domain-verification=t1rKCy68JFszSdCKVpw64A1QksWdXuYFUeSXKU"

internal.inlanefreight.htb. 604800 IN   TXT     "v=spf1 include:mailgun.org include:\_spf.google.com include:spf.protection.outlook.com include:\_spf.atlassian.net ip4:10.129.124.8 ip4:10.129.127.2 ip4:10.129.42.106 ~all"

internal.inlanefreight.htb. 604800 IN   NS      ns.inlanefreight.htb.

dc1.internal.inlanefreight.htb. 604800 IN A     10.129.34.16

dc2.internal.inlanefreight.htb. 604800 IN A     10.129.34.11

mail1.internal.inlanefreight.htb. 604800 IN A   10.129.18.200

ns.internal.inlanefreight.htb. 604800 IN A      10.129.34.136

vpn.internal.inlanefreight.htb. 604800 IN A     10.129.1.6

ws1.internal.inlanefreight.htb. 604800 IN A     10.129.1.34

ws2.internal.inlanefreight.htb. 604800 IN A     10.129.1.35

wsus.internal.inlanefreight.htb. 604800 IN A    10.129.18.2

internal.inlanefreight.htb. 604800 IN   SOA     inlanefreight.htb. root.inlanefreight.htb. 2 604800 86400 2419200 604800

;; Query time: 0 msec

;; SERVER: 10.129.14.128#53(10.129.14.128)

;; WHEN: So Sep 19 18:53:11 CEST 2021

;; XFR size: 15 records (messages 1, bytes 664)









##### Отдельные Aзаписи с именами 

##### хостов также можно 

##### получить с помощью 

##### атаки методом перебора

https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/subdomains-top1million-5000.txt





В качестве альтернативы можно выполнить команду for-loopв Bash, 

которая выведет список этих записей и отправит соответствующий 

запрос на нужный DNS-сервер.



SavitskiyES@htb\[/htb]$ for sub in $(cat /opt/useful/seclists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.inlanefreight.htb @10.129.14.128 | grep -v ';\\|SOA' | sed -r '/^\\s\*$/d' | grep $sub | tee -a subdomains.txt;done











ИЛИ DNSenum
---




SavitskiyES@htb\[/htb]$ dnsenum --dnsserver 10.129.14.128 --enum -p 0 -s 0 -o subdomains.txt -f /opt/useful/seclists/Discovery/DNS/subdomains-top1million-110000.txt inlanefreight.htb



dnsenum VERSION:1.2.6



-----   inlanefreight.htb   -----





Host's addresses:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_







Name Servers:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_



ns.inlanefreight.htb.                    604800   IN    A        10.129.34.136





Mail (MX) Servers:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_







Trying Zone Transfers and getting Bind Versions:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



unresolvable name: ns.inlanefreight.htb at /usr/bin/dnsenum line 900 thread 1.



Trying Zone Transfer for inlanefreight.htb on ns.inlanefreight.htb ...

AXFR record query failed: no nameservers





Brute forcing with /home/cry0l1t3/Pentesting/SecLists/Discovery/DNS/subdomains-top1million-110000.txt:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_



ns.inlanefreight.htb.                    604800   IN    A        10.129.34.136

mail1.inlanefreight.htb.                 604800   IN    A        10.129.18.201

app.inlanefreight.htb.                   604800   IN    A        10.129.18.15

ns.inlanefreight.htb.                    604800   IN    A        10.129.34.136



...SNIP...

done.














###### Перебор поддоменов



SavitskiyES@htb\[/htb]$ for sub in $(cat /opt/useful/seclists/Discovery/DNS/subdomains-top1million-110000.txt);do dig $sub.inlanefreight.htb @10.129.14.128 | grep -v ';\\|SOA' | sed -r '/^\\s\*$/d' | grep $sub | tee -a subdomains.txt;done



ns.inlanefreight.htb.   604800  IN      A       10.129.34.136

mail1.inlanefreight.htb. 604800 IN      A       10.129.18.201

app.inlanefreight.htb.  604800  IN      A       10.129.18.15































































ДОП ИНФО



https://wiki.debian.org/BIND9?action=show\&redirect=Bind9



















