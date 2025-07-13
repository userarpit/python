import numpy as np
import sys
import test

my_list = [1, 2, 3, 4]

# my_array = np.asarray(my_list)
my_array1 = np.array(my_list, dtype=complex)
my_array2 = np.array([1, 2, 3, 4], dtype=complex)
print(my_array1 * my_array2)
print(my_array1.ndim)
# print(my_array.size)
# print(type(my_array))
# print(my_array)
# print(my_array.dtype)
# print(my_array.shape)

# np_zeroes = np.zeros((10,5),dtype=int)
# print(np_zeroes)

# np_ones = np.ones((5,5),dtype=np.int32)
# print(np_ones)
# print(np_ones.shape)
# print(np_ones.size)
# print(np_ones.itemsize)

# np_range = np.arange(start = 2, step = 2, stop = 20)
# print(np_range)

# np_linspace = np.linspace (start = 2, stop=20, num = 4)
# print(np_linspace)

# np_random = np.random.random((5,5))
# print(np_random)

# np_reshape = np.reshape(np_range,(3,3),order='F')
# print(np_reshape)
# print(np.arange(10000).reshape(25,400))
# np.set_printoptions(threshold=sys.maxsize)
# print(np.arange(10000).reshape(50,200))

# A = np.asarray([[1,1],[0,1]])
# B = np.asarray([[2,0],[3,4]])
# print(A*B)
# print(A@B)
# print(A.dot(B))
# print(A.sum())
# print((A@B).sum())
# print((A@B).cumsum(axis=1))

# """
# print(np_reshape[2,1])
# np_cond = np_reshape[np_reshape > 5]
# print(np_cond)
# print(np_reshape > 5)

# print(np.insert(np_reshape,1,[2,3,4],axis=1))
# print(np.append(np_reshape,[[2,3,4],[1,1,1],[4,5,6]],axis=0))
# print(np.delete(np_reshape,[3,4]))
# print(np.delete(np_reshape,1,axis=0))
# print(np_reshape)
#  """
# print(np.prod([1, 3, 4], initial=5))
# print(A.flatten())
# """
# x = np.random.randint(5)
# print(x)
#  """


# full_array = np.full((3, 5), 102.10)
# print(np.eye(3)) # identity matrix

# for i in np.eye(3).flat:
#     print(i)

# print(full_array.reshape((-1,5)))
# full_array.resize((5,3))

# print(full_array)

# a = np.arange(12)**2
# i = np.array([1, 1, 3, 8, 5])
# print(a[i])

# j = np.array([[3, 4], [9, 7]])
# print(a[j])

# print(a.shape[0])
# print(a.shape)

print(np.arange(1, 10).reshape(3, 3))
print(np.arange(1, 24, 2).reshape(3, 2, 2))

A = np.arange(3, 12).reshape(3, 3)
print(A)
print(A.min())
print(A.max())
print(A.mean())

B = A**2
print(B)

C = np.vstack((A, B))
print(C)

D = C @ A
print(D)

print(C.reshape(3, 3, 2))
