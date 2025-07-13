import random
list35 = [x for x in range(1,1001) if (x % 5 == 0 and x % 7 ==0)]

# print(list35)
print(random.sample(list35,5))
