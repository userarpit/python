import numpy as np

data = np.array(
    [
        [10, 11, 12, 13],  # Row 0
        [20, 21, 22, 23],  # Row 1
        [30, 31, 32, 33],  # Row 2
        [40, 41, 42, 43],  # Row 3
    ]
)


print(data)

row_index = [1, 3, 2, 0]
col_index = [2, 3, 1, 0]

new_array = data[row_index, col_index]
print(new_array)
