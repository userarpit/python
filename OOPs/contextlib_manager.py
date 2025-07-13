from contextlib import contextmanager


@contextmanager
def managed_file(file_name):
    try:
        file = open(file_name, mode="w")
        yield file
    finally:
        file.close()


with managed_file("hello.txt") as file:
    file.write("hello hi arpit")
