class MyList:
    def __init__(self, *args):
        print("init")
        self._data = list(*args) if len(args) != 0 else []

    def __getitem__(self, index):
        print("getitem")
        return self._data[index]

    def __setitem__(self, index, value):
        print("setitem")
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        print("repr")
        return f"MyList({', '.join(repr(item) for item in self._data)})"
    
    def __delitem__(self, key):
        print("delitem")
        del self._data[key]

    def __iter__(self):
        print("iter")
        return iter(self._data)
    
    def __contains__(self, item):
        print("contains")
        return item in self._data

    def __mul__(self, n):
        print("mul")
        if isinstance(n, int):
            return MyList(self._data * n)
    
    def __rmul__(self, n):
        print("rmul")
        return self.__mul__(n)
    
    
my_list = MyList([1, 2, 3])
print(my_list)

print(len(my_list))
print(my_list[0])
my_list[0] = 10

print(my_list)
del my_list[1]
print(my_list)
print("-" * 100)
for item in my_list:
    print(item)
print("-" * 100)
print(3 in my_list)
print("*" * 100)
print(3 * my_list)