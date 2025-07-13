import numpy as np
list_ = [1,2,3,4,5]
# 1
list_array = np.array(list_)
print(np.sum(list_array))
print(np.prod(list_array))

# 2
q2 = np.arange(1,10).reshape((3,3))
print(q2)

#3
a = np.random.randint(1,100,(2,3))
print(a)
print(np.mean(a))
print(np.median(a))
print(np.std(a,axis=1))

#4
def sort_array(list1):
    # print(list1)
    arr_sort = np.array(list1)
    arr_sort.sort()
    return arr_sort

print(sort_array([2,3,4,1,56,23,45,87,65]))

# 5
list_of_list = np.random.randint(1,100,(5,5))
print(list_of_list)

print(np.sum(list_of_list,axis=0))
print(np.sum(list_of_list,axis=1))

# 6
max_min = np.random.randint(1,100,(4,4))
print(max_min)
print(np.max(max_min))
print(np.min(max_min))

#7
def square_array(array):
    return np.square(array)
arr1 = np.random.randint(1,100,(3,3))
print(arr1)
print(square_array(arr1))

#8
arr = np.random.randint(1,100,(2,2))
print(arr)
print(arr.dot(arr))

#9
arr = np.random.randint(1,100,(2,2))
print(arr)
print(np.invert(arr))

#10
def array_transpose(array) -> np.array:
    return array.transpose()

a_t = np.random.randint(1,100,(3,3))
print(a_t)
print(array_transpose(a_t))