import random
import argparse
import time


if __name__ == "__main__":
    # import argparse
    random.seed(444)
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--nprod", type=int, default=5)
    parser.add_argument("-c", "--ncon", type=int, default=10)
    ns = parser.parse_args()
    start = time.perf_counter()
    # asyncio.run(main(**ns.__dict__))
    print(ns.__dict__)
    elapsed = time.perf_counter() - start
    print(f"Program completed in {elapsed:0.5f} seconds.")