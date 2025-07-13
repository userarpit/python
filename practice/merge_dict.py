dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

# zs = {}
# zs.update(dict1)
# zs.update(dict2)
zs = dict(**dict1, **dict2)

# for k, v in dict2.items():
#     dict1[k] = v

print(zs)