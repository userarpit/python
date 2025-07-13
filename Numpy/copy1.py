import numpy as np

a = np.floor(20* np.random.random((3,4)))
print(a)

c = a.view()
c.resize(2,6)
print(c)
print(a.shape)
c[1,2] = 100
print(a)
