import threading
import time
# import logging


def thread_function(name):
    print("Thread start", name)
    time.sleep(2)
    print("Thread end", name)


def main() -> None:
    print("main start")
    threads = list()
    for index in range(3):
        x = threading.Thread(target=thread_function, args=(index,), daemon=True)
        x.start()
        threads.append(x)

    for index, thread in enumerate(threads):
        print("before join", index)
        thread.join()
        print("thread done.....", index)

    print("main end")
    # print(().name)


if __name__ == "__main__":
    main()
