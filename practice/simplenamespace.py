from types import SimpleNamespace

obj = SimpleNamespace(name="john", age=30)
print(type(obj))


obj.lastname="Khandelwal"
print(obj)


a = {1,2,3}
b = {4,5,6}

c = {frozenset(b)}
print(c)