import numpy as np

data = np.arange(1, 17).reshape(4, 4)


# data.reshape(4,4)
print(data)

mask = data > 10
print(mask)

print(data[mask])

row_filter_mask = data[:, 3] % 2 == 0
print(row_filter_mask)
print(data[row_filter_mask])

data[data % 2 != 0] = -1
print(data)
