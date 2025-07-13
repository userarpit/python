import numpy as np

np_array = np.array([[1,2],[6,8]])
print(np_array)
print(np_array.shape)

np_array_insert = np.insert(arr = np_array ,obj = 1,values=[3,4],axis=1)
print(np_array_insert)
print(np_array_insert.shape)

np_array_append = np.append(arr = np_array,values=[[3,4],[1,2]],axis=1)
print(np_array_append)

np_array_delete = np.delete(arr=np_array,obj=1,axis=1)
print(np_array_delete)
print(np_array_delete.shape)



