import numpy as np
a = 10 * np.random.rand(2,3)
b = 10 * np.random.rand(2,3)
# a = int(a)
print(a)
print(b)
# print(np.vstack((a,b)))
# print(np.hstack((a,b)))

print(a+b)
print(a*b)

a = np.random.randint(1,100,(2,3))
print(a)
print(np.mean(a))
print(np.median(a))
print(np.std(a,axis=1))

x = np.arange(1, 25).reshape(2, 12)
print(np.hsplit(x, (3, 4)))
print(np.random.random((2,2)))
c = np.ones((2,3))

print(np.unique(c,return_counts=True))
t = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 2, 3, 4]])
unique_rows, indices, occurrence_count = np.unique(
     t, axis=0, return_counts=True, return_index=True)

print(indices)
print(occurrence_count)