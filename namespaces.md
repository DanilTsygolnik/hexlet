## `__main__`


```python
class Person:
    '''Класс для хранения данных человека

    Attributes:
        name (str): person's name.
    '''
    name = 'Noname'


Person # <class '__main__.Person'>
person_bob # <__main__.Person object at 0x7f529d8a6dd0>
```

Обратите внимание на то, как отображается класс C при выводе в REPL: `<class '__main__.C'>`. Пространство имён, которое вы видите, когда запускаете REPL, так и называется — `__main__`, поэтому полное имя класса, который был объявлен в этом пространстве имён, содержит именно это имя модуля. Классы, созданные в именованных модулях, будут содержать полные имена модулей в тексте их (классов) полного имени. [^namespaces-hexlet]

[^namespaces-hexlet]: https://ru.hexlet.io/courses/python-oop-basics/lessons/classes/theory_unit
