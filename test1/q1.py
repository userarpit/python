a = [5, 6, 8, 9, 4, 'x', 'y', 9, 6, 4, 6, 7, 6]

# # print(a.__len__())
# print(len(a))
# print(a.count(6))

# b = [5,7,4,9]

# a += b

a = [2 if elem == 'x' else elem for elem in a]
a = [4 if elem == 'y' else elem for elem in a]

print(a)