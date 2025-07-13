import functools
from decorator import singleton

class CountCalls:
    def __init__(self, func) -> None:
        functools.update_wrapper(self,func)
        self.func = func
        self.count = 0

    def __call__(self,*args,**kwargs):
        self.count += 1
        print(f"call {self.count}")
        return self.func(*args,**kwargs)
    
@CountCalls
def say(name):
    print(f"hi {name}")
# say = CountCalls(say)
say("arpit") # call object say() say.__call__()
say("khandelwal")
        
@singleton
class One:
    pass

first = One()
second = One()
print(id(first))
print(id(second))
