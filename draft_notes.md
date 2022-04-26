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
