from decorators import do_twice, timer, debug
# import math


@do_twice
def say_whee():
    print("Whee!")


# greet = do_twice(greet)
@do_twice
def greet(name):
    print(name)
    return f"hi {name}"


say_whee()
a = greet("arpit")
print(a)


@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([number**2 for number in range(10_000)])


waste_some_time(1)
waste_some_time(999)


# make_greeting = timer(debug(make_greeting))
@timer
@debug
def make_greeting(name, age=None):
    if age is None:
        return f"howdy {name!r}"
    else:
        return f"{name} is {age} years old"


print("*" * 100)
print(make_greeting("Arpit", 38))

# math.factorial = debug(math.factorial)

# a = sum([math.factorial(num) for num in range(1, 10)])
# print(a)

# print(greet("arpit"))
