import random as rnd
import math as mth

# choice - random number from list
mylist = list(range(1,10))
print(rnd.choice(mylist))

#randrange - randome number from range
print(rnd.randrange(0,3000,5))

#random - randome between 0 and 1 (float)
print(rnd.random())

#seed - same random number
rnd.seed(10)
print(rnd.random());
print(rnd.random());

print(rnd.random());

#shuffle - shuffle the list, return none
print(mylist)
rnd.shuffle(mylist)
print(mylist)

#uniform - float randon number between range specified
print(rnd.uniform(4,7))

print(mth.pi)
print(mth.e)