import concurrent.futures as cf
import threading
import time


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        print(f"Thread start {name}")
        print(f"Thread {name} about to get lock. waiting.....")
        with self._lock:
            print(f"Thread {name} has lock")
            local_copy = self.value
            local_copy += 1
            time.sleep(5)
            self.value = local_copy
            print(f"value updated to {self.value}")
            print(f"Thread {name} about to release the lock")
        
        print(f"Thread {name} lock released")
        print(f"Thread end {name}")


def main():
    print("main start")
    database = FakeDatabase()

    print(f"start value is {database.value}")

    with cf.ThreadPoolExecutor(max_workers=5) as executor:
        for index in range(5):
            executor.submit(database.update, index)

    print(f"end value is {database.value}")
    print("main end")


if __name__ == "__main__":
    main()
