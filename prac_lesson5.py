# Пока мы не умеем наследовать классы, заглушаум сообщение
# линтера про "class without a base class" с помощью комментария
class RGB:  # noqa: WPS306.
    red = 0
    green = 0
    blue = 0


red, green, blue = RGB(), RGB(), RGB()
red.red = 255
green.green = 255
blue.blue = 255

