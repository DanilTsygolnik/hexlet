class Counter:
    '''
    Счетчик должен хранить неотрицательное целое значение,
    которое можно изменять.
    '''

    value = 0

    def inc(self, increment=1):
        self.value += increment

    def dec(self, decrement=1):
        if decrement > self.value:
            self.value = 0
        else:
            self.value -= decrement
