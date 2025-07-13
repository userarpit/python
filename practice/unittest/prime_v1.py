import math


def is_prime(number):
    if not isinstance(number, int):
        raise TypeError(f"integer number expected, got {type(number).__name__}")

    if number <= 1:
        raise ValueError(f"integer above 1 expected, got {number}")

    for i in range(2, int(math.sqrt(number) + 1)):
        # breakpoint()
        if number % i == 0:
            return False

    return True


# is_prime(-1)
