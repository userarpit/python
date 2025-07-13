import numpy as np
a = np.arange(10,dtype=int)
np.savetxt("numpy2.csv",a,delimiter=";")

load_array = np.loadtxt("numpy2.csv",delimiter=",")
print(load_array)