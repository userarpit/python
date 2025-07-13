list1 = [2, 3, 4, 5, 3, 5, 5, 2, 3, 7, 8, 9, 6, 3, 1, 3, 5, 7, 4]
list2 = [1, 3, 4, 5, 10]


print(set(list1) | set(list2))
print(set(list1) & set(list2))
print(set(list1) - set(list2))

list1 = ["ksdk", "ljoi", "ooihoieff"]
print(set(("".join(list1))))