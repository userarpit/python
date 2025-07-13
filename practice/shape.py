import math
from pympler import asizeof
class PositiveNumber:
    def __set_name__(self,owner,name):
        print("__set_name__")
        self._name = name

    def __get__(self,object,type = None) -> object:
        print("__get__")
        return object.__dict__.get(self._name)
    
    def __set__(self,object,value) -> None:
        print("__set__")
        if not isinstance(value, int | float) or value <= 0:
            raise AttributeError("Positive number expected")
        object.__dict__[self._name] = value

class Circle:
    radius = PositiveNumber()

    def __init__(self, radius) -> None:
        print("__init circle__")
        self.radius = radius
    
    def area(self):
        print("area circle")
        return math.pi * math.pow(self.radius, 2)
class Square:
    __slots__ = ["side"]
    # side = PositiveNumber()

    def __init__(self, side) -> None:
        print("__init square__")
        self.side = side
    
    def area(self):
        print("area square")
        return math.pow(self.side, 2)

c = Circle(10)
print(c.area())
# print(c.__dict__)
s = Square(10)
print(s.side)
# print(s.__dict__)
print(asizeof.asizeof(s))
print(Square.area(s))
print(Circle.area(c))    
print(Circle.__dict__)