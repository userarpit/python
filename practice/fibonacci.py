from decorator import count_calls, cache
import functools

# fibonacci = cache(count_calls(fibonacci))
@functools.cache
@count_calls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci (num -2)
    
print(fibonacci(10))
# fibonacci = cache(count_calls(fibonacci))
# print(fibonacci.count)
print(fibonacci(8))
# print(fibonacci(5))
# print(fibonacci(11))