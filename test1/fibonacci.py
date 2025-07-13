fibolambda =  lambda a,b : a + b

def fibonacci(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    x = int(input("Enter number "))
    generatorfibo = fibonacci(x)
    for i in generatorfibo:
        print(i,end=" ")