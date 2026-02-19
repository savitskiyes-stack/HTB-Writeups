SMTP commands

nc 10.129.12.164 25 — Подключение к SMTP-серверу на порт 25 для ручного взаимодействия (получение баннера, ввод команд)
telnet mail1.inlanefreight.htb 25 — Подключение по FQDN (если в /etc/hosts)



EHLO mail1.inlanefreight.htb — Инициация с FQDN лабы, для активации расширений
HELO mail1.inlanefreight.htb — Приветствие с FQDN для имитации локального клиента
VRFY root@infreight.com — Проверка существования пользователя (код 252/250 — возможно существует)
RCPT TO: <infreight-admin@inlanefreight.htb> — Проверка получателя в транзакции (250 Ok — существует)
MAIL FROM: <test@external.com> — Произвольный отправитель (250 Ok)
DATA — Начало тела письма
Subject: Test — Заголовок (часть тела).
This is a test message. — Тело.
. — Конец письма (250 Ok: queued as ID)
RSET — Сброс транзакции (250 Ok, для следующей проверки)
QUIT — Закрытие сессии



smtp-user-enum -M RCPT -U wordlist.txt -D inlanefreight.htb -t 10.129.12.249 — Enumeration с методом RCPT и словарем



openssl s_client -starttls smtp -crlf -connect 10.129.12.164:25 — Подключение с STARTTLS для проверки сертификата




Итог, для определения VRFY не работает(выдает 252 на всех пользователей), проверка через отправку не дала результатов также у всех пользоватлей 250. Проверка enum по перебору, все пользователи валидны. При отправке писем на пользователя robin@infreight.htb единственого не вернуло ошибку о доставке. Пользователь подтвержден. 











