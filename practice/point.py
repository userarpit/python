class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self,value):
        self._x = _validate(value)

    @y.setter
    def y(self,value):
        self._y = _validate(value)

def _validate(value):
    if not isinstance(value, int | float):
        raise ValueError("number expected")
    return value


p = Point(3,5)
print(p.x)
print(p._x)
print(p.y)
print(p._y)
p.y = '10'
        