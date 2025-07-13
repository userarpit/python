from matplotlib import pyplot as plt
import numpy as np


seasons = {
    "Winter": 12,
    "Spring": 19,
    "Summer": 28,
    "Fall": 9
}

plt.bar(seasons.keys(), seasons.values())
plt.xlabel("seasons")
plt.ylabel("People")
# plt.savefig("fruit.jpg")
# plt.legend("")
plt.show()


# plt.hist(random.randn(10000), 20)
# plt.show()
