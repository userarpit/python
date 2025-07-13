import copy


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{type(self).__name__}({self.x!r}, {self.y!r})"


class Rectangle:
    def __init__(self, topleft, bottomright):
        self.topleft = topleft
        self.bottomright = bottomright

    def __repr__(self):
        return f"{type(self).__name__}({self.topleft!r}, {self.bottomright!r})"


A = Point(10, 23)
B = copy.copy(A)
print(A)
print(B)
print("*" * 10)
A.x = 99
print(A)
print(B)
print("-" * 10)

rect = Rectangle(Point(0, 0), Point(10, 10))
srect = copy.deepcopy(rect)
print(rect)
print(srect)
rect.topleft.x = 99
print(rect)
print(srect)
