import threading
import time
# import logging


def thread_function(name):
    print("Thread start", name)
    time.sleep(2)
    print("Thread end", name)

def main() -> None:
    print("main start")
    x = threading.Thread(target=thread_function, args=(1,), daemon=True)
    x.start()
    x.join()
    print("main end")
    # print(().name)
if __name__ == "__main__":
    main()