


### Lesson 3

Tests


Чем по сути является HTTP? -- Искусственным общим языком для передачи данных
Это является особенностью HTTP версии 1.1? -- Возможность повторно использовать TCP-соединение вместо создания нового соединения при каждом запросе
Код 301 в теле ответа - это код ответа.


Practice

Используя telnet выполните запрос к hexlet.local (расположен на localhost) на порт 8080. Параметры запроса: метод GET, страница /, протокол HTTP 1.1;

```
telnet localhost 8080
# in telnet
GET / HTTP/1.1
host: hexlet.local
```

### Lesson 4

```
Content-Length: 218 # bytes
Content-Type: application/octet-stream
```

Tests

Что должен содержать ответ при выполнении запроса с использованием глагола HEAD? -- Только заголовки.
Какое значение содержится в поле "Content-Length" в ответе (response)? -- количество байт занимаемое телом ответа.
Content-Length может присутствовать и в запросе, и в ответе.

[Practice](prac_lesson4.md) 

### Lesson 5

tests

В какой части HTTP-запроса находятся данные формы при ее отправке глаголом POST? -- в теле
Как разделяются названия полей формы в HTTP-запросе если она отправлена GET-глаголом? -- `&`
Может ли ответ на HTTP-запрос (то есть HTTP response) содержать тело с какой-то информацией? -- да, может.

Practice

Выполните авторизацию на сайте hexlet.local (расположен на localhost:8080).
Для этого отправьте на url `/session/new` следующие данные формы:
- username со значением `admin`;
- password со значением `secret`.
Используйте глагол `POST` и тип `application/x-www-form-urlencoded`.

```
telnet localhost 8080
# in telnet
POST /session/new HTTP/1.1
Host: hexlet.local
Content-Type: application/x-www-form-urlencoded
Content-Length: 30
Connection: close

username=admin&password=secret
```

### Lesson 6

tests

С чего начинается каждый chunk? - число, указывающее размер chunk'a
Чем заканчивается каждый chunk? - символ перевода строки CRLF
Каким образом обозначается последний chunk? -- он нулевой длины, после него — двойной перевод строки
В случае с передачей ответа с помощью chunks, каким образом тело ответа отделяется от заголовков? - как обычно — два перевода строки

Practice

Используя telnet выполните запрос к hexlet.local (расположен на localhost) на порт 8080. Параметры запроса: глагол GET, страница /stream, протокол HTTP 1.1

```
telnet localhost 8080
# in telnet
GET /stream HTTP/1.1
Host: hexlet.local
Connection: close
```
Результат запроса:
```
HTTP/1.1 200 OK
X-Powered-By: Express
Transfer-Encoding: chunked
Connection: close
Date: Thu, 14 Apr 2022 17:26:48 GMT

59
Noliwpe witil puwmav riersaw gemilemid ger hel ujaer fajej zog rezzemhid seg pahug uriti.
5d
Jemarga rikle diodi zopog wu wegoteji vunlotek anuazi vaiteka ik leazi hilledta soti gogriop.
60
Gesro monrozhof podohu gobna wukep efbof gihubhi fuf tej pur mentuus be newlahfi jezse dolpubew.
5b
Tapuw la siw pod kovetbaf mokuto la as uninar ojah si epezijaj bugsut otoenfim bomigwev de.
53
Fa oh potlawsip ve igpec ovzuvum enemevsu jab irogekog tojki oma wen dosew ti dute.
0

Connection closed by foreign host.
```
### Lesson 7


query string для GET-запросов на выборку без изменения данных. В частности, чтобы была возможность создать ссылку на результат запроса (?)

tests

Какой из типов запросов должен использоваться только для получения данных и не должен приводить к изменениям данных? -- GET
Какой из типов запросов лучше всего поддается кэшированию (если запросы используются правильно)? -- из POST и GET - это GET
Возможно ли в одном запросе передавать данные и в body, и в request line с помощью query string? - Да (? потому что несвязанные параметры ??)
Запрос публикует новый комментарий в блоге. Является ли такой запрос идемпотентным? - нет, т.к. происходит изменение данных


Practice

Используя telnet выполните запрос к hexlet.local (расположен на localhost) на порт 8080. Передайте в строке запроса следующие параметры:
- key равный value
- another_key равный another_value.
Параметры запроса: глагол GET, страница /, протокол HTTP 1.1

```
telnet localhost 8080
# in telnet
GET /?key=value&another_key=another_value HTTP/1.1
Host: hexlet.local
Connection: close
```

### Lesson 8

Location - ключевое поле в body, в случае редиректа (код 301/302), т.к. хранит адрес, куда переходить.

tests

Возможно в ответ 301 включить тело? -- да (но это, в сущности, неважно)
При ответе "301" новый адрес указан в поле "Location". Чем является это поле? -- одним из заголовков
Возможно ли делать редирект на страницу, которая в свою очередь содержит новый редирект на другую страницу? -- да

practice

Используя telnet выполните запрос к hexlet.local (расположен на localhost) на порт 8080.
Параметры запроса: глагол POST, страница /session/new, протокол HTTP 1.1

```
telnet localhost 8080
# in telnet
POST /session/new HTTP/1.1
Host: hexlet.local
Connection: close
```
Результат запроса:
```
HTTP/1.1 302 Found
X-Powered-By: Express
Connection: close
Location: /
Vary: Accept
Content-Type: text/plain; charset=utf-8
Content-Length: 23
Date: Thu, 14 Apr 2022 17:57:34 GMT

Found. Redirecting to /
Connection closed by foreign host.
```

### Lesson 9

tests

Какой код используется для обозначения запрета доступа без аутентификации ("access denied")? -- 401
Форму для базовой аутентификации генерирует сам браузер (это не HTML-форма; не создается на стороне сервера)
Возможно ли применить базовую аутентификацию только к одной странице на сайте? -- да

practice

Используя telnet авторизуйтесь на hexlet.local (расположен на localhost:8080).
Параметры запроса: 
- глагол GET
- страница /admin
- протокол HTTP 1.1
- имя пользователя Aladdin
- пароль open sesame

Подготовим строку `login:password` в шифровке (?) base64. В терминале:
`printf 'Aladdin:open sesame' | base64`

Получаем строку: `QWxhZGRpbjpvcGVuIHNlc2FtZQ==`

Запрос:
```
telnet localhost 8080
# in telnet
GET /admin HTTP/1.1
Host: hexlet.local
Authorization: Basic QWxhZGRpbjpvcGVuIHNlc2FtZQ==
Connection: close
```
Пример ответа при успешной авторизации:
```
HTTP/1.1 200 OK
X-Powered-By: Express
Connection: close
Date: Thu, 14 Apr 2022 18:20:11 GMT
Content-Length: 14

Access granted
Connection closed by foreign host.
```

Если ввести неверную последовательность в поле Authorization:
```
HTTP/1.1 401 Unauthorized
X-Powered-By: Express
Connection: close
WWW-Authenticate: Basic realm='Admin Panel'
Date: Thu, 14 Apr 2022 18:17:55 GMT
Content-Length: 13

Access denied
Connection closed by foreign host.
```

### Lesson 10

tests

HTTP — stateless protocol. Что это значит? -- каждая пара «HTTP-запрос + ответ» независимая, и протокол не «помнит» ничего о прошлых запросах
Может ли заголовок "Set-cookie" встречаться несколько раз в одном ответе (response)? -- может
Где у пользователя хранятся cookie, отправленные сервером? -- в браузере (по факту, постоянные - на винте, сессионные - в оперативной памяти ??)
В куки есть такой фрагмент: `domain = .yandex.ru`. Для каких адресов будет использоваться этот куки? -- для `yandex.ru` и всех поддоменов вида `x.yandex.ru`
Пользователь зашел на сайт интернет-магазина (без авторизации, как гость), добавил несколько товаров в свою корзину, закрыл браузер, перезагрузил компьютер, открыл браузер, вернулся на сайт и увидел, что товары все еще находятся в его корзине. Какой тип cookie использовался (скорее всего) для достижения такого эффекта? -- персистентные куки (persistent cookies); не сессионные куки (session cookies)

practice

Используя telnet выполните запрос к hexlet.local (расположен на localhost) на порт 8080. Параметры запроса: глагол GET, страница /account, протокол HTTP 1.1, куки name со значением user и secret со значением secret_hash;

```
telnet localhost 8080
# in telnet
GET /account HTTP/1.1
Host: hexlet.local
Cookie: name=user
Cookie: secret=secret_hash
Connection: close
```
