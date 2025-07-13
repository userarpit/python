import threading
import time
# import logging


def thread_function(name, semaphore):
    if semaphore.acquire(timeout=4):
        try:
            print("Thread start", name)
            time.sleep(2)
        finally:
            print("Thread end", name)
            semaphore.release()
    else:
        print(f"{name} did not get the lock")


def main() -> None:
    semaphore = threading.Semaphore()
    print("main start")
    threads = list()
    for index in range(3):
        x = threading.Thread(
            target=thread_function, args=(index, semaphore), daemon=True
        )
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
