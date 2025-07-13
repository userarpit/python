import functools
from decorator import slow_down, singleton

@singleton
class CountCalls:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__}()")
        return self.func(*args, **kwargs)

# say_whee = CountCalls(say_whee)
# say_whee = slow_down(rate=4)(CountCalls(say_whee)))
# @slow_down(rate=1)
@CountCalls
def say_whee():
    print("whee")


say_whee()
say_whee()
print(say_whee.num_calls)
A = CountCalls(say_whee)
B = CountCalls(say_whee)

print(A is B)

