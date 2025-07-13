import math
from decorator import timer, singleton
# @singleton
class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self,value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("radius must be non-negative")
    
    @property
    def area(self):
        return self.pi() * self.radius**2
    
    @classmethod
    def unit_circle(cls):
        return cls(1)
    
    @staticmethod
    @timer
    def pi():
        return math.pi
    
c = Circle(10)
# print(c.radius)
# c.radius = 20
# print(c.radius)
# print(c.area)

# unit_circle_circle = Circle.unit_circle()
# print(unit_circle_circle.radius)
# print(unit_circle_circle.area)