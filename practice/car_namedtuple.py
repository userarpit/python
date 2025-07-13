from collections import namedtuple

Car = namedtuple("Car", ["color", "mileage"])


class MyCarWithMethods(Car):
    __slots__ = ()

    def hexcolor(self):
        if self.color == "Red":
            return "#ff0000"
        else:
            return "#000000"


c = MyCarWithMethods("Red", 1234)
print(c.hexcolor())
print(Car._fields)
ElectricCar = namedtuple("ElectricCar",  Car._fields + ('charge',), defaults=[0.0])

print(ElectricCar('red', 1234))
print(c._asdict())