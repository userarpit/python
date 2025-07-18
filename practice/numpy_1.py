import numpy as np

arr = np.array([[1, 2], [3, 4]])
print("Array:\n", arr)
print("Shape:", arr.shape)
print("Dtype:", arr.dtype)
print("Ndim:", arr.ndim)
print("Size:", arr.size)
print("*" * 100)
tensor = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])
# print(f"Tensor:\n{tensor}")
# # print(tensor.size)
# print(tensor[0][:])

print(tensor.shape)
print(tensor.reshape(9, 1))
print(tensor)

array_1d = np.array([1, 2, 3, 4, 5, 6])
# print(array_1d.ndim)
array_2d = array_1d.reshape(2, 3)
print(array_2d)
print(array_2d.ndim)


print(array_1d[2::2])
print(array_2d[array_2d > 2])
print("*" * 100)
rows = np.array([0, 1])
cols = np.array([0, 1])
print(array_2d)
print(array_2d[rows, cols])  # Accessing specific elements using row and column indices
# print(df['A'].values.shape)

print("*" * 100)

arr1d_a = np.array([1, 2, 3])
arr1d_b = np.array([4, 5, 6])

stack_axis = np.stack((arr1d_a, arr1d_b), axis=0)
print("stack 1D arrays along axis 0 (rows):\n", stack_axis)

stack_axis1 = np.stack((arr1d_a, arr1d_b), axis=1)
print("\nstack 1D arrays along axis 1 (columns):\n", stack_axis1)
