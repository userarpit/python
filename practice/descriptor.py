class OneDigitNumericValue:
    def __init__(self):
        self.value = {}

    def __get__(self, obj, type=None) -> object:
        try:
            return self.value[obj]
        except:
            return 0
        
    def __set__(self, obj, value) -> None:
        if value > 9 or value < 0 or int(value != value):
            raise AttributeError("Value is invalid")
        self.value[obj]= value

class Foo:
    number = OneDigitNumericValue()

first = Foo()
first.number = 3
print(first.number)
second = Foo()
print(second.number)