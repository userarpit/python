from datetime import datetime
import random
from decorator import do_twice, timer, register, PLUGINS, repeat, slow_down

def not_during_the_night(func):
    def wrapper_not_during_the_night():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass
    return wrapper_not_during_the_night



@do_twice
# @regis
def greet(name):
    print(f"Hello {name}")
    return "hi"

# greet = do_twice(greet)    
print(greet("Arpit"))
print(greet)
print(greet.__name__)

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])
# waste_some_time = timer(waste_some_time)

waste_some_time(1)
waste_some_time(999)

@register
def say_hello(name):
    return f"Hello {name!r}"

@register
def be_awesome(name):
    return f"Yo {name!r}, together we're the awesomest!"

greeter, greeter_func = random.choice(list(PLUGINS.items()))
print(greeter_func('Alice'))
print(globals())

# @repeat(5)
@slow_down(rate=5)
def name(name):
    print(name)
# name = repeat(5)(name)
name("Arpit")
name("Khandelwal")