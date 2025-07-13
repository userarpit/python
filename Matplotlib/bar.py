from matplotlib import pyplot as plt
import numpy as np

from numpy import random

# centers = np.arange(1, 6)
# tops = np.arange(2, 11, 2)

fruits = {
    "apples": 10,
    "oranges": 16,
    "bananas": 9,
    "pears": 4
}

plt.bar(fruits.keys(), fruits.values())
plt.xlabel("Fruits")
plt.ylabel("Count")
plt.savefig("fruit.jpg")
plt.show()

# plt.hist(random.randn(10000), 20)
# plt.show()
