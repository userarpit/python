import numpy as np
arr1 = np.random.randint(1,100,(5,6))
arr2 = np.random.randint(1,100,(1,6))

print(arr1)
print(arr2)
print(arr1 + arr2)

from numpy import array, argmin, sqrt, sum
observation = array([111.0, 188.0])
codes = array([[102.0, 203.0],
               [132.0, 193.0],
               [45.0, 155.0],
               [57.0, 173.0]])
diff = codes - observation    # the broadcast happens here
dist = sqrt(sum(diff**2,axis=-1))
print(diff)
print(sum(diff**2,axis=-1))
print(argmin(dist))

a = diff.view()
print(diff)
print(a)
c = a.ravel()
c[1] = 99
print(a)