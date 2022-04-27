# Настройка виртуального окружения

По материалам:
-[виртуальные окружения (hexlet)](https://ru.hexlet.io/courses/python-setup-environment/lessons/venv/theory_unit) 
-[How To Install Python 3 and Set Up a Local Programming Environment on Ubuntu 20.04](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-ubuntu-20-04#step-2-setting-up-a-virtual-environment) 


# Этапы разработки

## Установка flask в виртуальное окружение

Окружение `flask_env` в отдельном терминале
`source py_environments/flask_env/bin/activate`

```bash
python3 -m pip install flask
python3 -m pip list
```

## Index page

Чему научился:
- программирование обработчика статических путей;
- использование шаблонизатора;

## Обработчики hello и greet

Чему научился:
- программирование обработчика динамических путей (работа с переменными);
- использование функции `escape()` для обработки строковых переменных в адресе (защита от XSS-атак)[^xss-atack];

[^xss-atack]: https://owasp.org/www-community/attacks/xss/

Использованные материалы:
- [генерация URL и переход по ссылки при нажатии кнопки](https://www.geeksforgeeks.org/how-to-insert-a-javascript-variable-inside-href-attribute/);
- [HTML Style Guide (indentation)](https://www.w3schools.com/html/html5_syntax.asp);
-[HTML-тэги для формы](https://www.w3schools.com/html/html_forms.asp);
- [пример использования javascript-функции в форме](https://stackoverflow.com/a/42679710);

## Калькулятор

Использованные материалы:
- считывание значения выбранной radio-button; [^get-selected-radio-value]

[^get-selected-radio-value]: links
    1. https://stackoverflow.com/a/17796775
    2. https://stackoverflow.com/a/24886483

Дополнительные просмотренные материалы:
- переход по ссылке при нажатии на кнопку -- javascript; [^button-url-js]

[^button-url-js]: ссылки
    1. https://stackoverflow.com/questions/32423594/how-to-use-submit-button-to-go-to-a-url-with-html
    2. https://stackoverflow.com/questions/2701041/how-can-i-set-the-form-action-through-javascript
    3. https://stackoverflow.com/questions/30282714/add-javascript-onclick-to-html-form-submit


### Вопросы

В таком виде функция не возвращает url, хотя по идее должна: [^js-concat]
```javascript
function get_result_url() {
    var num1 = document.getElementById('num1').value;
    var num2 = document.getElementById('num2').value;
    var operator = document.querySelector('input[name = "operator"]:checked').id;
    var url = "calc/";
    return url.concat(operator, "/", num1, "/", num2);
}
```

[^js-concat]: links
    1. https://www.techonthenet.com/js/string_concat.php
    2. https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Strings

---

Каким образом работать с типом `float`? Обработчик не работает при следующей записи, хотя по докам [^flask-quickstart] тип допускается:
```python
@app.route('/calc/<operator>/<float:num1>/<float:num2>/')
def calc_result(operator, num1, num2):
    ...
```

---

Я вывожу отдельные "индексные" страницы (index, hello, calc) через шаблон, что несовсем логично. А как еще можно? Как правильно?
