### Nmap Scripting Engine ( NSE) функция Nmap для создания скриптов 

### на Lua и взаимодействия с определёнными сервисам





+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| Категория      | Описание                                                                                                                                      |

+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

| auth           | Определение учетных данных для аутентификации.                                                                                                |

| broadcast      | Скрипты, используемые для обнаружения хостов путем широковещательной рассылки, и обнаруженные хосты могут быть автоматически добавлены к остальным сканированиям. |

| brute          | Выполняет скрипты, которые пытаются войти в соответствующую службу путем подбора учетных данных методом перебора.                              |

| default        | Скрипты, выполняемые по умолчанию с помощью этой -sCопции.                                                                                    |

| discovery      | Оценка доступности услуг.                                                                                                                     |

| dos            | Эти скрипты используются для проверки сервисов на наличие уязвимостей типа «отказ в обслуживании» и применяются реже, поскольку наносят вред сервисам. |

| exploit        | Эта категория скриптов пытается использовать известные уязвимости сканируемого порта.                                                         |

| external       | Скрипты, использующие внешние сервисы для дальнейшей обработки.                                                                               |

| fuzzer         | Этот метод использует скрипты для выявления уязвимостей и некорректной обработки пакетов путем отправки различных полей, что может занимать много времени. |

| intrusive      | Вредоносные скрипты, которые могут негативно повлиять на целевую систему.                                                                     |

| malware        | Проверяет, не заражена ли целевая система вредоносным ПО.                                                                                     |

| safe           | Защитные скрипты, которые не осуществляют навязчивый и деструктивный доступ.                                                                  |

| version        | Расширение для обнаружения сервисов.                                                                                                          |

| vuln           | Выявление конкретных уязвимостей.                                                                                                             |

+----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+












Способы определения необходимых скриптов в файле Nmap





Скрипты по умолчанию

\[!bash!]$ sudo nmap <target> -sC





Категория конкретных скриптов

\[!bash!]$ sudo nmap <target> --script <category>







Определенные скрипты

\[!bash!]$ sudo nmap <target> --script <script-name>,<script-name>,...





Nmap — Агрессивное сканирование

\[!bash!]$ sudo nmap 10.129.2.28 -p 80 -A

-A	Выполняет обнаружение служб, определение операционной системы, трассировку маршрута и использует скрипты по умолчанию для сканирования целевого объекта.





Nmap - Категория уязвимостей

\[!bash!]$ sudo nmap 10.129.2.28 -p 80 -sV --script vuln 

--script vuln	Использует все связанные скрипты из указанной категории.



Обновить базу данных скриптов NSE
SavitskiyES@htb[/htb]$ sudo nmap --script-updatedb




Найти скрипты на системе
SavitskiyES@htb[/htb]$ find / -type f -name ftp* 2>/dev/null | grep scripts






Сканирование FTP сервера:
SavitskiyES@htb[/htb]$ sudo nmap -sV -p21 -sC -A 10.129.14.136




















Nmap scan report for 10.129.2.28

Host is up (0.036s latency).



PORT   STATE SERVICE VERSION

80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))

| http-enum:

|   /wp-login.php: Possible admin folder

|   /readme.html: Wordpress version: 2

|   /: WordPress version: 5.3.4

|   /wp-includes/images/rss.png: Wordpress version 2.2 found.

|   /wp-includes/js/jquery/suggest.js: Wordpress version 2.5 found.

|   /wp-includes/images/blank.gif: Wordpress version 2.6 found.

|   /wp-includes/js/comment-reply.js: Wordpress version 2.7 found.

|   /wp-login.php: Wordpress login page.

|   /wp-admin/upgrade.php: Wordpress login page.

|\_  /readme.html: Interesting, a readme.

|\_http-server-header: Apache/2.4.29 (Ubuntu)

|\_http-stored-xss: Couldn't find any stored XSS vulnerabilities.

| http-wordpress-users:

| Username found: admin

|\_Search stopped at ID #25. Increase the upper limit if necessary with 'http-wordpress-users.limit'

| vulners:

|   cpe:/a:apache:http\_server:2.4.29:

|     	CVE-2019-0211	7.2	https://vulners.com/cve/CVE-2019-0211

|     	CVE-2018-1312	6.8	https://vulners.com/cve/CVE-2018-1312

|     	CVE-2017-15715	6.8	https://vulners.com/cve/CVE-2017-15715

<SNIP>





Доп инфо о скриптах:
https://nmap.org/nsedoc/index.html




































































































