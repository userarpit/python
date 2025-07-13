import numpy as np

X, Y = [int(x) for x in input("enter 2 values with space in between - ").split(" ")]

lst1 = list(range(1,16 * X, X))
lst2 = list(range(1,16 * Y, Y))

np1 = np.array(lst1)
np2 = np.array(lst2)

np1 = np.reshape(np1,(4,4))
np2 = np.reshape(np2,(4,4))
print(np1)
print(np2)
np3 = np.subtract(np1, np2)

print(np3.ravel())
