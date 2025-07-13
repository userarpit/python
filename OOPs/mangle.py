_Mangled__A = 99
class Mangled:
    def __init__(self):
        self.__A = 100
    
    # def call(self):
    #     self.
        
    def __print(self):
        print("print")

    def call(self):
        return self.__A

    def __call__(self, *args, **kwds):
        print(args[1])


m = Mangled()
print(m._Mangled__A)
# m._Mangled__print()
print(dir(m))
print(m.call())
m(32, 33)
print(m._Mangled__A)


