class HourClock:
    def __init__(self, current_hour: int = 0):
        self.time = current_hour % 12

    @property
    def hours(self):
        return self.time

    @hours.setter
    def hours(self, value: int):
        new_time = value % 12
        self.time = new_time
