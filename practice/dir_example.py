import operator


class A:
    def __dir__(self):
        return [1, 2, 3]

    def printa(self, a):
        return "abc"


a = A()
print(dir(a))
i = 10
print(operator.le(i, 20))

# print(x + "asd")

# a.printa()
a = "arpit"
# print(a[34])
print(a.lower())
# print(a.__dir__())
mytable = a.maketrans("a", "A")
print(mytable)
print(a.translate(mytable))
