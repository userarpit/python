import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# print(np.dot(A,B))
print(A)
# print(B)
# print(A * B)

# print(A.T)

print(A_inv := np.linalg.inv(A))

print(A @ A_inv)
det_A = np.linalg.det(A)

print(det_A)

# Example 3.3: Eigenvalues and Eigenvectors
matrix_e = np.array([[4, 2], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(matrix_e)

print(eigenvalues)
print(eigenvectors)