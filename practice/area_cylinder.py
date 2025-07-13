from decorator import set_unit
import math


@set_unit("CM^3")
def volumn(radius, height):
    return math.pi * radius**2 * height


# print(volumn(3,3))
print(f"The volumn of cylinder is {volumn(3,3):.2f} {volumn.unit}")
