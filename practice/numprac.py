import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
arr = np.arange(1,11).reshape(2,5)
print(arr)
print(np.flip(arr))
print(np.flip(arr,axis=1))
print(arr.shape)
arr[1] = np.flip(arr[1])
print(arr)  
arr[:,2] = np.flip(arr[:,2])
print(arr)

arr_flatten = arr.flatten()
arr_flatten[1] = 2000
print(arr)
print(arr_flatten)
arr_ravel = arr.ravel()
arr_ravel[1] = 99
print(arr)
# print(arr?)

np.save('file',arr)
b = np.load("file.npy")
print(b)
np.savez('file',arr,b,arr_flatten)
outfiles = np.load('file.npz')
print(outfiles)
for i in outfiles:
    print(outfiles[i])

df = pd.DataFrame(arr)
print(df)
df.to_csv("data.csv")

np.savetxt('np.csv', arr, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')
plt.plot(arr.flatten())
plt.show()

