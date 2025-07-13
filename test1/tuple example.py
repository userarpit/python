tup = (1,2,3)
print(tup)
tup1 = (10,20,30)
#deleting tuple
del tup
try:
    print(tup)
except:
    print("catch tuple")

print(tup1)

my_list = [10,22,235]
tup1 = tuple(my_list)
print(tup1[2])
print(max(tup1))
print(min(tup1))
print(len(tup1))