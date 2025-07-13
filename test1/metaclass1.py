'''
A class functions as a template for the creation of objects, 
A metaclass functions as a template for the creation of classes. 
Metaclasses are sometimes referred to as class factories.
'''


class Meta(type):
    def __new__(cls,name,bases,dict):
        x = type.__new__(cls,name,bases,dict)
        x.attr = 110
        return x

class Foo(metaclass = Meta):
    pass

print(Foo.attr)
print(Foo.__base__)
print(Foo.__class__)