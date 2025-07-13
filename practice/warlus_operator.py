# import random
# def return_value() -> int:
#     return random.randint(0,10)

# if (x := return_value()) > 4:
#     print(f"inside If = {x}")

# print(f"outside if = {x}")


numbers = [1, 2, 3, 4, 5]
squared = [y ** 2 for x in numbers if (y := x ** 2) > 10]
print(squared)