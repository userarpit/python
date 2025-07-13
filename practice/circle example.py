import math

class Circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return math.pi * pow(self.radius,2)

    def circumference(self):
        return 2 * self.radius * math.pi
    
c = Circle(10)
print(c.area())
print(c.circumference())