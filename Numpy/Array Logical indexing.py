import numpy as np

my_list = [[1, 5, 3], [4, 1, 6], [2, 4, 10]]

np_array = np.array(my_list)
print(np_array[2, 2])
np_cond = np_array[np_array > 3]
print(np_cond)
print(np_array > 3)

a = np.arange(10) ** 3
print(a)
print(a[1:4])
print(a[::-1])
print(a[:6:2])
a[:6:2] = 1000
print(a)

b = np.fromfunction(lambda x, y: 10 * x + y, (3, 3), dtype=int)
print(b)
print(b[0:2, 1])
print(b[:, 2])
print(b[1, ...])

print(np_array @ np_array)
print(np.matmul(np_array, np_array))
print(np_array.shape)
print(np_array.mean())