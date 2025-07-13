import functools
lst = [1, 2, 3, 5, 9, -4]

sum = functools.reduce(lambda x, y: x + y, filter(lambda x: x > 0, lst))
print(sum)
