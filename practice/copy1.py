import copy

matrix1 = [[1, 2], [3, 4]]
print(matrix1)

matrix2 = copy.deepcopy(matrix1)
matrix2[1][0] = 10

print(matrix1)
print(matrix2)
