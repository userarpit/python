from collections import namedtuple


def custom_divmod(a, b):
    DivMod = namedtuple("DivMod", "quotient, remainder")
    return DivMod(*divmod(a, b))


print(custom_divmod(34, 6))
