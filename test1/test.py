import datetime
import time
import pdb
import sys
import timeit
current_timestamp = time.time()

timestamp = current_timestamp  # Example timestamp
datetime_object = datetime.datetime.fromtimestamp(timestamp)

datetime_object = str(datetime_object)
datetime_object = datetime_object.replace(":","-")
datetime_object = datetime_object.replace(".","-")
print(datetime_object)


import keyword
    
print(keyword.kwlist)
# pdb.set_trace()
testDict = {i: i * i for i in range(10)}
print(testDict)
print(sys.version)
print(sys.hexversion)



testList = [10,20,30]


def test(x,y,z):
    print(x,y,z)
    
test(*testList)

import functools
fact = functools.reduce(lambda x,y: x*y,range(1,5))
result = (lambda k: functools.reduce(int.__mul__, range(1,k+1),1))(5)

print(fact)
print(result)

test = [1,2,3,4,4,2,4,1,1,1,1]
print(max(set(test),key=test.count))
# print(max(set(test), key=test.count))

#-> 4
print(sys.getrecursionlimit())

n=0

def recu_limit(n):
    if n == 1:
        print("n is 1")
        return
    recu_limit(n-1)
    
# recu_limit(5)

sys.setrecursionlimit(3000)
# recu_limit(4967)

print(sys.getsizeof(10))
print(recu_limit.__code__.co_consts)
print(recu_limit.__code__.co_varnames)
print(recu_limit.__code__.co_names)

import dis
print(dis.dis(recu_limit))


print('create_database_query time - ' + 
      str(timeit.timeit(stmt='recu_limit(1)',
                        setup = 'from __main__ import recu_limit',number=100)))

print('create_database_query time - ' + 
      str(timeit.repeat(stmt='recu_limit(1)',repeat=2,
                        setup = 'from __main__ import recu_limit',number=100)))
