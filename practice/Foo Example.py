class Foo:
    def getter(self) -> object:
        print("accessing the attribute to get the value")
        return 42
    
    def setter(self,x) -> None:
        print("accessing the attribute to set the value")
        raise AttributeError("cannot change the value")
    
    x = property(getter,setter)

f = Foo()
print(f.x)
print(type(f).__dict__)