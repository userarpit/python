# # def say_hello(name):
# #     return f"Hello {name}"
import functools
import time

# # def be_awesome(name):
# #     return f"Yo {name}, together we're the awesomest!"


# # def greet_bob(greeter_func):
# #     return greeter_func("Bob")


# # # print(greet_bob(say_hello))

# def parent():
#     print("Printing from parent()")

#     def first_child():
#         print("Printing from first_child()")

#     def second_child():
#         print("Printing from second_child()")

#     second_child()
#     first_child()


def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(a, b):
        print("Something is happening before the function is called.")
        func(a, b)
        print("Something is happening after the function is called.")

    return wrapper_decorator


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


# my_name = decorator(my_name)
@decorator
def my_name(first, last):
    print(f"My name is {first} {last}")


if __name__ == "__main__":
    my_name("Arpit", "Khandelwal")
# say_whee = decorator(say_whee)


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time

        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_args = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_args)
        print(f"calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value

    return wrapper_debug
