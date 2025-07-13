class OneDigitNumericValue:
    # def __init__(self,name) -> None:
    #     print("init")
    #     self.name = name
    
    def __set_name__(self,owner,name):
        print(owner)
        print(name)
        self.name = name

    def __get__(self,obj,type=None) -> object:
        print("get")
        return obj.__dict__[self.name]
    
    def __set__(self,obj,value) -> None:
        print("set")
        obj.__dict__[self.name] = value

class Number:
    one = OneDigitNumericValue()

n = Number()
n1 = Number()

n.one = 20
n1.one = 30
print(n.__dict__)
print(n1.__dict__)
print(n.one)
