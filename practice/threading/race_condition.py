import concurrent.futures as cf
import threading
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0

    def update(self, name):
        print(f"Thread start {name}")
        local_copy = self.value
        local_copy += 1
        time.sleep(1)
        self.value = local_copy
        print(f"Thread end {name}")


def main():
    print("main start")
    database = FakeDatabase()

    print(f"start value is {database.value}")

    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)

    print(f"end value is {database.value}")
    print("main end")


if __name__ == "__main__":
    main()
