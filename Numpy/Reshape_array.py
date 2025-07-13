import numpy as np

np_array = np.arange(20)
np_array_reshape = np.reshape(np_array,(5,4),order="F")

print(np_array)
print(np_array_reshape)

#np_array_reshape = np.reshape(np_array,(2,4),order="F")

print(np_array_reshape[2,3])

my_list = list(np_array)
# modify
my_list[1] = 5
np_array[1] = 6

# access
print(my_list[1])
print(np_array[1])

my_list_reshape = list(np_array_reshape)

#print(my_list_reshape[1,3])
print(my_list_reshape[1][3])
print(np_array_reshape[2,3])
print(np_array_reshape[2][3])

print(np.mean(np_array))
print(np.median(np_array))
#print(np.mode(np_array))
