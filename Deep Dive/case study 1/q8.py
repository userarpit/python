import math
a = list(map(int,input("Enter numbers seprated by comma - ").split(",")))
print(a)

output = list(map(lambda x: int(math.sqrt((100 * x) / 30)),a))
print(output)
