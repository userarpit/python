my_list = [10,3.4,24,35,35]
print(my_list)
del my_list[2]
print(my_list)

print(len(my_list))
print(max(my_list))
print(min(my_list))

list_2 = ['arpit','khandelwal']

#extend
my_list.extend(list_2)
print(my_list)
#count
print(my_list.count(35))

#index
print(my_list.index(35))
#reverse
print(my_list)
my_list.reverse()
print(my_list)

#sort
my_list_2 = ['Ford','Mitsubishi','BMW','VW']
def func(a):
    return len(a)

my_list_2.sort(reverse=True,key=func)
print(my_list_2)