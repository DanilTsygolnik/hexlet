
## Lesson 4

Как называют сущности, доступные в пределах программы в единственном экземпляре? - Одиночки

Что стоит знать об атрибутах модулей и классов, представляющих собой ссылки на изменяемые объекты?
- Их стоит использовать с опаской (легко запутывают код, упрощают внесение ошибок)
- Отлаживать код, изменяющий такие объекты — сложно (изменения атрибутов класса приводит к изменению значений атрибутов во всех экземплярах класса, которых м.б. много)

## Lesson 5

Как называется процесс (акт) создания объекта по образу и подобию класса? - Инстанцирование

Как называется объект, созданный на основе класса? - Экземпляр (instance)

Какое имя имеет атрибут, используемый объектной системой Python для хранения атрибутов?
```python
# имя - __dict__
bob.__dict__['name'] # 'Bob'
```

Выберите допустимые способы проверки принадлежности объекта к некоему классу.
```python
class Person:
    pass
 
bob = Person()


# способ 1
bob.__class__ is Person # True

# способ 2, рекомендованный
isinstance(bob, Person) # True
```

## Lesson 6

Как называются методы, знающие, к какому объекту они "присоединены"? - Связанные

Выберите корректные вызовы метода append, которые успешно добавят в список `my_list` в качестве значения пустой список `[]`.
```python
my_list = []
# связанный метод
my_list.append([])
# метод класса list
list.append(my_list, [])
```

Как называют аргумент, получающий при вызове метода объекта ссылку на этот объект?
```python
# аргумент self
class Foo:
    def bar(self):
        pass
```

## Lesson 7

Как правильно называется метод `__init__`? - Инициализатор (а не конструктор, т.к. работает с существующим в памяти объектом).

Что делает метод `__init__`? - Выполняет первоначальную настройку только что созданного объекта ( а конструктор в других ЯП -- Выделяет память для объекта и настраивает его ?? )

В чем суть "утиной" типизации (duck typing)? - 

Как называется договорённость между стороной, ожидающей наличия некоторых методов у объекта, и классом, предоставляющим эти методы? - Протокол (пример - функция `len()`, которая "ожидает" наличия метода `__len__` в атрибутах объекта некоторого класса).

## Lesson 8

Какие методы могут быть ассоциированы со свойством? - getter, setter, deleter

Можно ли создать свойство, которое будет иметь только setter? - можно, 2 способа:
1) с использованием декоратора
2) с использованием вызова `property(fset=func_name)`
```python
# способ 1
class Foo:
    @ property
    def bar(self):
        return 'baz'

# способ 2
def bar(self):  # отдельно функция для getter'a
    return 'baz'

class Foo:
    bar = property(fget=bar)
```

Укажите правильный декоратор, превращающий метод в setter свойства bar?
```python
class Foo:
    @property
    def bar(self):
        return 'baz'

    # правильный декоратор
    @bar.setter
    def bar(self, new):
        pass
```

## Lesson 10

Какие варианты конструкции try являются правильными?
```python
try:
    ...
except Foo:
    ...


try:
    ...
except Foo:
    ...
except Bar:
    ...
finally:
    ...


try:
    ...
finally:
    ...
```

Какие варианты описания обработчика синтаксически верны?
```python
# не рекомендуется, нужно конкретно указывать
except:
    ...
except (Foo, Bar) as e:
    ...
except Exception as e:
    ...
```

Как правильно заново возбудить только что пойманное исключение?
```python
try:
    ...
except Exception as e:
    ...
    # correct way
    raise
```

## TODOs

- [ ] lesson 7 -- duck typing