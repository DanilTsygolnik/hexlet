class Counter:
    '''
    Счетчик должен хранить неотрицательное целое значение,
    которое можно изменять.
    '''

    def __init__(self, val=0):
        self.value = val

    def inc(self, increment=1):
        new_value = self.value + increment
        return Counter(new_value)

    def dec(self, decrement=1):
        new_value = 0
        if decrement < self.value:
            new_value = self.value - decrement
        return Counter(new_value)

