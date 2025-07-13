from collections import namedtuple
from dataclasses import dataclass, astuple
from pympler import asizeof

Point = namedtuple("Point", "x y z")
p = Point(10, 20, 30)

print(asizeof.asizeof(p))
print("dataclasses below")

@dataclass(frozen=True)
class Point1:
    # __slots__ = ["x", "y", "z"]
    x: int
    y: int
    z: int

    def __iter__(self):
        return iter(astuple(self))


p1 = Point1(1, 2, 3)
print(asizeof.asizeof(p1))
print(p1.x)
# p1.x = 0

for a in p1:
    print(a)

print(asizeof.asizeof(p))
print(asizeof.asizeof(p1))
# print(p1.__dict__)