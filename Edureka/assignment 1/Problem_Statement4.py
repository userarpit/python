import numpy as np

ls1  = [int(x) for x in input("Enter array 1 of 3 * 3 with space in between - ").split(" ")]
ls2  = [int(x) for x in input("Enter array 2 of 3 * 3 with space in between - ").split(" ")]

arr1 = np.array(ls1)
arr2 = np.array(ls2)

arr3 = np.subtract(arr1,arr2)
arr3 = np.reshape(arr3,(3,3))
print(arr3)