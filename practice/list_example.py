list1 = [1, 2, 3, 4]
list2 = ['abv', 'fghqwwwwww', 'cdfgg', 1, 2, 3, 4, 1, 2, 3, 5, 1, 2, 3, 4]
list4 = ['adfdd', 'adgf', 'adhad', 'adirr', 'tyuuj']

print(min(list1))

print(list(map(lambda i: i * i, list1)))

list3 = [i for i in list1 if i in list2]
print(list3)

# word = max(list2, key=len)
# print(word, len(word))

dict1 = {}
for i in list2:
    dict1[i] = list2.count(i)

print(dict1)

list_name = ['arpit', 'lksk', 'iiurm', 'arpit']
print(set(list_name))

print(sorted(list4))

if list4 == sorted(list4):
    print("True")
else:
    print("False")
    
lista = [1,2,3,4,5,6]
listb=[5,6,7,3,5,67,5,6]
print(set(lista + listb))
