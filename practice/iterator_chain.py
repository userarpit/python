def integer():
    for i in range(9):
        yield i


def square(seq):
    for s in seq:
        yield s * s


def negate(seq):
    for num in seq:
        yield -num


for num in negate(square(integer())):
    print(num, end=" ")

print("\nusing generator expression")

integer = range(9)
square = (s * s for s in integer)
negate = (-num for num in square)
print(list(negate))