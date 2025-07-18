import functools
import time


def timer(func):
    """Decorator to time the execution of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Function '{func.__name__}' executed in {end_time - start_time:.4f} seconds")
        return result
    return wrapper


# test=timer(test)
@timer
def test(name: str) -> None:
    time.sleep(4)
    print(f"Hello {name} from test function in functions.py")
    name = "arpit"


if __name__ == "__main__":
    name = "khandelwal"
    test(name)
    