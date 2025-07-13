class Multibases(type):
    def __new__(cls,clsname,bases,dict):
        if len(bases) > 1:
            raise TypeError("More than 1 base class")
        return super().__new__(cls,clsname,bases,dict)

class Base(metaclass=Multibases):
    pass

class A(Base):
    pass

class B(Base):
    pass

class C(A,B):
    pass