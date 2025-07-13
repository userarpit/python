import threading
import time


from typing import NoReturn


def say_hello(name: str) -> NoReturn:
    """This function prints a hello message to the console with the given
    name. The name is the only argument of the function and it must be a
    non-empty string.

    Parameters
    ----------
    name : str
        The name of the person to greet. This parameter must be a non-empty
        string. If the parameter is empty, the function will raise a ValueError.
    """
    # Check if the name is a string
    if not isinstance(name, str):
        # if the name is not a string, raise a TypeError
        raise TypeError("The name must be a str")

    # Check if the name is empty
    if not name.strip():
        # if the name is empty or whitespace, raise a ValueError
        raise ValueError("The name must not be empty")

    # If the name is valid, print a hello message with the given name
    print(f"Hello {name!r}")


def main() -> None:
    """
    This function is the entry point of the program. It will start the timer
    that will print a message every 2 seconds.
    """
    event = threading.Event()

    timer = threading.Timer(2, say_hello, args=["Arpit"])

    while not event.is_set():
        # start the timer
        timer.start()

        # wait for 10 seconds before stopping the timer
        time.sleep(10)

        # stop the timer
        event.set()


if __name__ == "__main__":
    main()
