
import sys
import cProfile

num_squared_lc = [num**2 for num in range(1,10000)]
num_squared_gc = (num**2 for num in range(1,10000))

print(sys.getsizeof(num_squared_gc))
print(sys.getsizeof(num_squared_lc))
print(cProfile.run('sum(num_squared_gc)'))
print(cProfile.run('sum(num_squared_lc)'))

def infinite_sequence(end=0) -> int:
    num = 0
    while num < end:
        p = (yield int(num))
        num += 1
        print(p)

print("*" * 100)

is_iter = infinite_sequence(end=1000)

for i in is_iter:
    print(i)
    # is_iter.send(100)
    if i > 50:
        is_iter.close()
        
    # print("-"* 10)