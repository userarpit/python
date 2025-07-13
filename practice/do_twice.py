import functools
from typing import Callable


def twice(func: Callable[[str, str], str]):
    @functools.wraps(func)
    def wrapper_twice(*args, **kwargs):
        for _ in range(2):
            value = func(*args, **kwargs)
        return value

    return wrapper_twice


@twice
def create_greeting(*name: str) -> str:
    for n in name:
        print(f"Hello {n}")


create_greeting("Arpit", "Shanaya")
