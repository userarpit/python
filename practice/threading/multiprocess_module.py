import multiprocessing as mp
import time
import os


def fact(n):
    print(os.getpid(), end=" ")
    return 1 if (n == 1 or n == 0) else n * fact(n - 1)


def long_running_task() -> None:
    print("Process started")
    time.sleep(5)
    print("process finished")


if __name__ == "__main__":
    # p = mp.Process(target=fact)
    start = time.perf_counter()
    # for num in range(1, 1000):
    #     print(fact(num))

    # pool = mp.Pool(processes=2, maxtasksperchild=2)
    pool = mp.Pool()
    result = pool.map(fact, range(3, 6))
    # p.start()
    end = time.perf_counter()
    print(f"Total {end-start}")
    # p.join()

    # print(result)
