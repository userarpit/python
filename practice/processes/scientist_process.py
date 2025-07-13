from collections import namedtuple
import multiprocessing as mp
import time

Scientist = namedtuple("Scientist", ["name", "field", "born", "nobel"])

scientists = (
    Scientist(name="Ada", field="math", born=1815, nobel=False),
    Scientist(name="Emmy", field="english", born=1835, nobel=False),
    Scientist(name="Marie", field="math", born=1845, nobel=False),
    Scientist(name="Tu", field="math", born=1855, nobel=False),
    Scientist(name="Admin", field="art", born=1865, nobel=False),
    Scientist(name="Vera", field="math", born=1875, nobel=False),
    Scientist(name="Sally", field="math", born=1915, nobel=False),
)
# print(scientists)

def transform(x):
    time.sleep(1)
    # print(x)
    result = {"name": x.name, "age": 2017 - x.born}
    # breakpoint()
    return result

if __name__ == "__main__":

    start = time.time()

    pool = mp.Pool(processes=len(scientists))
    result = pool.map(transform, scientists)
    # print(transform(scientists[0]))
    end = time.time()
    print(tuple(result))

    print(f"Duration {end-start:.2f}")
