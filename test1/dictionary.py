dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8 # update existing entry
dict['School'] = "DPS School" # Add new entry
print( "dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])

del dict['Class']
print(dict)

# dict.clear() to clear whole dictionary

print(len(dict))
str1 = str(dict)
print(str1[3:6])

print(type(dict))
dict1 = dict.copy()
dict.clear()
print(dict1)
print(dict)

# fromkeys
keys = [1,2,3]
values = 10
print(dict1.fromkeys(keys,values))

if 'Name1' in dict1:
    print("True")

print(dict1.items())
print(dict1.keys())
print(dict1.values())

print('%(Company)s is a %(Department)s Portal.' %{'Company': "GFG", 'Department': "CS"})

dict1.update({"Company":"AGK"});
print(dict1)
