## Задание

Используя telnet выполните запрос к hexlet.local (расположен на localhost) на порт 8080. Параметры запроса: глагол POST, страница /upload, протокол HTTP 1.1, тело: `my request body`. Не забудьте установить заголовки необходимые для отправки body;

Так как в теле запроса мы передаём обычный текст, нужно использовать тип `text/plain`

---

Команда для подключения:
```
telnet localhost 8080
```

Текст запроса:
```
POST /upload HTTP/1.1
Host: hexlet.local
Content-Type: text/plain
Content-Length: 15
Connection: close

my request body
```
