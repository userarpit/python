for t in int, float, dict, list, tuple:
    print(type(t))

def square(self,x):
    return x * x

Person = type('Person', (Exception, ), dict(Name="Arpit", squ=square))

p1 = Person()
print(p1.__class__)
#print(p1.__bases__)
print(p1.__dict__)

print(p1.Name)
print(p1.squ(2))