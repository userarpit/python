class rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, value):
        self._length = value

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    def area(self):
        # print("rectangle area")
        return self._length * self._width


class Square(rectangle):
    def __init__(self, length):
        super().__init__(length, length)


class VolumeMixin:
    def volume(self):
        return self.area() * self.height


class Cube(VolumeMixin, Square):
    def __init__(self, length):
        super().__init__(length)
        self.height = length

    def face_area(self):
        return super().area()

    def surface_area(self):
        return super().area() * 6


cube = Cube(2)
print(cube.surface_area())
print(cube.volume())

s = Square(4)
s.width=5
print(s.area())