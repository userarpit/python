class Addition:
    def __init__(self,a):
        self.a = a
   
    def __add__(self,obj):
        return self.a + obj.a

a = Addition(10)
b = Addition(20)

print(a+b)