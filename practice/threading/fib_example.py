import time


def main():
    start = time.perf_counter()
    for _ in range(20):
        print(f"run {_}")
        fib(35)

    print(f"Total time {time.perf_counter() - start}")


def fib(number: int) -> int:
    return number if number < 2 else fib(number - 1) + fib(number - 2)


if __name__ == "__main__":
    main()
