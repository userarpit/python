print("a")


def A() -> None:
    print("inside A")
# print(dir(__builtins__))
x = "arpit"
print(__name__)
def main(a: str):
    x = "kkkkk"
    print(x)
    
    print(locals())
    b=locals()
    b['key']='value'
    print(b)
    print(locals())
    number=99
    print(b)
    print(locals())
    
    A()
    f()

def f():
    # global y
    y=10
    print(locals())
    print(globals())

    def g():
        nonlocal y
        y = 20
    print(y)
    g()
    print(y)


if __name__ == '__main__':
    main("Khandelwal")