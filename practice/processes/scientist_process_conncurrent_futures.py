from collections import namedtuple
import concurrent.futures as cf
import time
import os
import pprint

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
pprint.pprint(scientists)

def transform(x):
    print(os.getpid())
    time.sleep(1)
    breakpoint()
    # print(x)
    
    result = {"name": x.name, "age": 2017 - x.born}
    return result

if __name__ == "__main__":

    start = time.time()

    with cf.ThreadPoolExecutor() as executor:
        result = executor.map(transform, scientists)
    # print(transform(scientists[0]))
    end = time.time()
    print(tuple(result))

    print(f"Duration {end-start:.2f}")
