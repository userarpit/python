class EvenNumber:
    def __set_name__(self,owner,name):
        print(name)

        self.name = name

    def __get__(self, obj, type = None) -> object:
        return obj.__dict__.get(self.name) or 0
    
    def __set__(self,obj,value) -> None:
        obj.__dict__[self.name]= (value if value % 2 == 0 else 0)

class Values:
    value1 = EvenNumber()
    value2 = EvenNumber()
    value3 = EvenNumber()
    value4 = EvenNumber()
    value5 = EvenNumber()

v = Values()
v.value1 = 1
v.value2 = 2
v.value3 = 3
v.value4 = 4
v.value5 = 5
print(v.value1)
print(v.value2)
print(v.value3)
print(v.value4)
print(v.value5)
# print(v.__dict__)