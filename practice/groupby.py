from itertools import groupby

fruit = ["apple", "anbcf", "lkjhfg", "banana", "cherry", "apoit", "ppooekdndnf"]
fruit.sort()
for k, group in groupby(fruit, key=len):
    print(k, (list(group)))
