import numpy as np

x = np.array([('Rex',9,81.0),('Fido',3,27.0)],dtype=[('name','U10'),('age','i4'),('weight','f4')])
print(x.dtype)
print(x[1])
print(x['age'])