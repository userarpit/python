# Python program to demonstrate unzip (reverse
# of zip)using * with zip function

# Unzip lists
l1, l2 = zip(*[('Aston', 'GPS'),
               ('Audi', 'Car Repair'),
               ('McLaren', 'Dolby sound kit')
               ])

# Printing unzipped lists
print(l1)
print(l2)

list1 = [1, 2, 3, 4]
list2 = [4, 5, 6]

combined_list = zip(list1, list2)
# print(type(combined_list))

# print(list(combined_list))
for elem1, elem2 in combined_list:
    print(elem1, elem2)

# print(list(combined_list))
