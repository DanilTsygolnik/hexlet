## Для чего нужен протокол HTTP

Прежде всего, важно помнить: работа по протоколу HTTP возможна только при условии, что есть два устройства, между которыми возможен обмен данными. В частности, подключение может производиться по IP-адресу, что возможно благодаря протоколу TCP.

Обмен данными между подключенными устройствами происходит по клиент-серверной модели: клиент запрашивает данные, сервер - возвращает ответ на запрос. Протокол HTTP можно рассматривать как набор правил и инструкций, позволяющих организовать обмен данными по клиент-серверной модели посредством команд.

<img src="https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjhiOTMzMTY4ZWI2NjdkNmNjOGRmODZmZGU2MjdlNjQwLnBuZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=5194f38baadb85d854331c7daae000cb21765cfe7c28f2ec5ad9b02c675db277">

В роли клиента может выступать, например, браузер или подпрограмма.

## Простейший HTTP-запрос

```
HEAD / HTTP/1.0
```

Запрос состоит из одной строки, которая называется _request line_.

Из чего состоит запрос:
- `HEAD` - специально слово (АКА глагол), от него зависит результат запроса;
- `/` - _request URI_, путь к ресурсу (в данном случае, корень сайта);
- `HTTP/1.0` - версия протокола.

TODO: записать выполнение запроса в терминале, добавить пояснение по двойному переносу строки ??

## HTTP/1.1

Данная версия протокола расширяет возможности предыдущей. Во времена создания протокола было принято, что одному доменному имени соотетствует едиственный IP-адрес. В настоящее время это не так, и нужно знать, к какому именно виртуальному хосту подключаться.

При использовании протокола HTTP/1.1 простейший запрос состоит уже из двух строчек:
```
HEAD / HTTP/1.1
Host: hexlet.io
```
где строка `Host: hexlet.io` - это т.н. _заголовок_.

При использовании версии HTTP/1.1 заголовок `Host` обязателен, иначе ответ не гарантирован.

В соответствии со [стандартом](https://www.ietf.org/rfc/rfc2616.txt) HTTP, заголовки отделяются друг от друга разделителем CRLF (он же строка "\r\n"; байты в формате HEX: 0x0D, 0x0A).

Маркером окончания ввода запроса является два разделителя CRLF подряд. По-простому, чтобы отправить запрос, после ввода последнего заголовка нужно дважды нажать Enter.

Еще одним отличием версии HTTP/1.1 от HTTP/1.1 является вводимое по умолчанию понятие `keep-alive`. Благодаря ему соединение TCP не обрывается после очередного HTTP-запроса, как в случае с HTTP/1.0 Соединение сохраняется ^[постоянное HTTP-соединение: https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%BD%D0%BE%D0%B5_HTTP-%D1%81%D0%BE%D0%B5%D0%B4%D0%B8%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5]либо до таймаута, либо пока не поступит явное указание на разрыв.

<img src="https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjE5MGM4ZGJjNDhiZjI2MjRjNWUwMzA5ODBhNGI1OGEzLmpwZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=f2b893a592a3d1a1dae7a23dad9faa15110c312edeb0bf81d99de0b33b843d2a">

В последнем случае в запрос нужно добавить заголовок `Connection`:
```
HEAD / HTTP/1.1
Host: google.com 
Connection: close
```

Результат запроса:
```
HTTP/1.1 301 Moved Permanently
Location: http://www.google.com/
Content-Type: text/html; charset=UTF-8
Date: Fri, 15 Apr 2022 17:15:32 GMT
Expires: Sun, 15 May 2022 17:15:32 GMT
Cache-Control: public, max-age=2592000
Server: gws
Content-Length: 219
X-XSS-Protection: 0
X-Frame-Options: SAMEORIGIN

Connection closed by foreign host.
```

## Тело запроса

До сих пор рассматривался запрос `HEAD`, не предусматривающий в ответе никакой информации, кроме содержащейся в заголовках.

Структура полного HTTP-запроса (как _request_, так и _response_) выглядит сл. образом:
<img src="https://cdn2.hexlet.io/derivations/image/original/eyJpZCI6IjMxZTc2ZjA3YzM3ODRkYjRmMTc1ZWM1MzIwM2FkMjljLmpwZyIsInN0b3JhZ2UiOiJjYWNoZSJ9?signature=16c68b9825c16810e7e1f0535fc3c3cdcbee02c18e378a4ece3eb3c1e3ef8325">

К примеру, так выглядит _response_ на запрос `GET`:
```
telnet hexlet.io 80

GET / HTTP/1.1
Host: hexlet.io

HTTP/1.1 301 Moved Permanently
Cache-Control: private
Content-Type: text/html; charset=UTF-8
Referrer-Policy: no-referrer
Location: https://34.102.241.4/
Content-Length: 218
Date: Tue, 07 Jul 2020 03:50:16 GMT

<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="https://34.102.241.4/">here</A>.
</BODY></HTML>
```

## Способ передачи данных №1 (через тело запроса)

Чтобы сформировать запрос, содержащий некоторую информацию в _body_, требуется заполнить следующие заголовки:
- `Content-Length` - размер вводимых данных (число байтов);
- `Content-Type` - тип данных, передаваемых в _body_.

[Пример запроса](prac_lesson4.md) 

[Дополнительные материалы](request_body_extra_info.md)

## Семантика глаголов, или два принципиально разных вида запросов

Идемпотентные (POST) и нет (GET)


## Передача данных через query string
[блок по query strings](https://ru.hexlet.io/courses/http_protocol/lessons/query_string/theory_unit)

TODOs:
- [ ] [польза понимания протокола http](https://ru.hexlet.io/courses/http_protocol/lessons/about/theory_unit)
- [ ] [встроить ссылку по DNS в коснпект](https://ru.hexlet.io/courses/http_protocol/lessons/http_1_0/theory_unit); еще раз просмотреть материал - м.б. что-то не дописал
- [ ] [блок по отправке форм в конспект](https://ru.hexlet.io/courses/http_protocol/lessons/forms/theory_unit)
- [ ] [блок по Transfer encoding и chunks](https://ru.hexlet.io/courses/http_protocol/lessons/chunked/theory_unit)
- [ ] перенаправления
- [ ] базовая аутентификация
- [ ] куки
