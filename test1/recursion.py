import os
from math import factorial
def fact(x):
    """recursive function for factorial"""
    if x == 1:
        return 1
    else:
        return x * fact(x-1)

print(fact(2))
print(fact(4))
print(fact(6))
print(fact(8))
print(factorial(10))
print(os.getcwd())
