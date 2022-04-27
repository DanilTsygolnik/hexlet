# Flask, проект №1

В рамках знакомства с основами микрофреймворка Flask написал свое первое web-приложение.

Необходимый теоретический минимум подчерпнул из учебных материалов Hexlet[^hexlet-courses], а закрепить все на практике побудил [гайд](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3).

[^hexlet-courses]: курсы
    - "Ключевые аспекты веб-разработки";
    - "Протокол HTTP";
    - "Python: Веб-разработка (Flask)".

### Краткое описание результатов

Это проект уровня "Hello, world!", и чтобы наработки смотрелись не слишком уныло, я немного усложнить задачу и добавить немного интерактива с помощью форм на отдельных web-страницах.

<img src="images/web_pages_scheme.png">

Главная страница:

<img src="images/index.png">

С главной страницы пользователь может перейти к одной из двух форм:

<img src="images/hello_form.png">
<img src="images/calc_form.png">

Пользователь заполняет форму и нажимает на кнопку отправки. Происходит отправка запроса на сервер. Запрос содержит URL, включающий данные, введенные пользователем. Программа-обработчик (функция на Python) использует эти данные для заполнения шаблона web-страницы, которую сервер вернет в ответ клиенту (то, что отрисуется в браузере после отправки формы).

<img src="images/hello_form_result.png">
<img src="images/calc_form_result.png">

Для калькулятора, в обработчике предусмотрена проверка исключительной ситуации "деление на ноль". В этом случае пользователь получит соответствующее сообщение:

<img src="images/hello_form_zero_div_result.png">

---

[Отчет о проделанной работе](noted.md)
