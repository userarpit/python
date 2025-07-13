import time
import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, *kwargs)
        return func(*args, *kwargs)

    return wrapper_do_twice


def repeat(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                wrapper_repeat.count += 1
                value = func(*args, **kwargs)
            print(f"{func.__name__} called {wrapper_repeat.count} times")
            return value

        wrapper_repeat.count = 0
        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)

    # return decorator_repeat


""" define timer decorator"""


def timer(func):
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        # print(type(start_time))
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__}() in {run_time:.4f} secs")
        return value

    return wrapper_timer


PLUGINS = dict()


def register(func):
    PLUGINS[func.__name__] = func
    return func


def slow_down(_func=None, *, rate=2):
    """sleep given amount of time before calling function"""

    def decorator_slow_down(func):
        @functools.wraps(func)
        def wrapper_slow_down(*args, **kwargs):
            time.sleep(rate)
            print(1)
            return func(*args, **kwargs)

        return wrapper_slow_down

    if _func is None:
        return decorator_slow_down
    else:
        return decorator_slow_down(_func)


def singleton(cls):
    functools.wraps(cls)

    def wrapper_singleton(*args, **kwargs):
        if wrapper_singleton.instance is None:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


def count_calls(func):
    functools.wraps(func)

    def wrapper_count_calls(*args, **kwargs):
        wrapper_count_calls.count += 1
        value = func(*args, **kwargs)
        print(f"call count {wrapper_count_calls.count}")
        return value

    wrapper_count_calls.count = 0
    return wrapper_count_calls


def cache(func):
    functools.wraps(func)

    def wrapper_cache(*args, **kwargs):
        key = args
        # print(key)
        if key not in wrapper_cache.cachedic:
            wrapper_cache.cachedic[key] = func(*args, **kwargs)
        return wrapper_cache.cachedic[key]

    wrapper_cache.cachedic = {}
    return wrapper_cache


def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # print(args)
        args_repr = [repr(a) for a in args]
        kwargs_args = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_args)
        print(f"calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__}() returned {repr(value)}")
        return value

    return wrapper_debug


def set_unit(unit):

    def decorate_set_unit(func):
        func.unit = unit
        return func

    return decorate_set_unit
