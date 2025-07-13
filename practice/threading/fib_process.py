from concurrent.futures import ProcessPoolExecutor
import time


def fib(number: int) -> int:
    return number if number < 2 else fib(number - 1) + fib(number - 2)


def main():
    start = time.perf_counter()

    with ProcessPoolExecutor() as executor:
        executor.map(fib, [35] * 20)

    print(f"Total time {time.perf_counter() - start} seconds")


if __name__ == "__main__":
    main()
