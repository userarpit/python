# decorate 2 numbers by square them, and then do sum and square root in the actual function
from math import sqrt


def square(func):

    def inner(a: int, b: int):

        return func(a**2, b**2)

    return inner


@square
def hypotenuse(first_int: int, second_int: int) -> float:
    """
    square root of sum of 2 numbers
    """
    return sqrt(first_int + second_int)

# hypotenuse = square(hypotenuse)


if __name__ == "__main__":
    print(hypotenuse(3, 4))
