dict = {}
dict1 = {}
dict['Name'] = "Arpit"
dict['Age'] = 38
dict1['Address'] = "Louisville"
dict1['Age'] = 39
print(dict)

dict1['State'] = "KY"

print(dict1)
# print(dict.update(dict1))
# new_dict = {**dict, **dict1}
new_dict = dict | dict1
print(new_dict)

# print(dict.copy())
print(dict.items() | dict1.items())

# list1 = 

list1 = [2, 3, 4, 5, 3, 5, 5, 2, 3, 7, 8, 9, 6, 3, 1, 3, 5, 7, 4]

print(set(list1))
freq = {}

for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
print(freq)
# print(sorted(freq))

for key, value in freq.items():
    print(key, value)

# new_dict = dict(sorted(freq.items(), key=lambda item: item[1]))
new_list = [(k, v) for k, v in new_dict.items()]
print(new_list[-1])
prin(new_dict)
del new_dict[2]
print(new_dict)

