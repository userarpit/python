class Repeater:
    def __init__(self, value, max_time):
        self.value = value
        self.max_time = max_time
        self._count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._count >= self.max_time:
            raise StopIteration
        self._count += 1
        return f"{self.value} - {self._count}" 


_repeater = Repeater("Hello", 5)
for r in _repeater:
    print(r)
