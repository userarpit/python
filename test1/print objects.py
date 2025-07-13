# If no __str__ method is defined, print t (or print str(t)) uses __repr__. 
# If no __repr__ method is defined then the default is used. 

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return "from repr {} & {}".format(self.name,self.age)

    def __str__(self) -> str:
        return "from str {} & {}".format(self.name,self.age)

Arpit = Person("Arpit",36)

print(Arpit)
print([Arpit])