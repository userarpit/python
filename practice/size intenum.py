from enum import IntEnum
class Size(IntEnum):
    S=1
    M=2
    L=3
    XL="4"

print(Size.XL.value <= Size.M.value)
print(type(Size.XL.value))