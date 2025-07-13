import numpy as np

np_arr = np.array([[2,3],[4,10]])
np_arr_broad = np_arr *5
print(np_arr_broad)

np_five = np.array([[5,6],[7,8]])
np_arr_nobroad = np_arr * np_five
print(np_arr_nobroad)

print(np_arr_broad.shape)

data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])

print(data)
print(data.shape)

multiply_by = np.array([1.2, 3.4, 2, 5])
print(multiply_by.shape)

# row_offset = multiply_by.reshape(4,1)
# print(row_offset)
print(data * multiply_by)