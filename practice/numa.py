import numpy as np
from io import StringIO

print(np.diag([1, 2, 3], 0))

print(np.vander([1, 2, 3, 5], 5, increasing=True))

A = np.ones((2, 2))
B = np.eye(2, 2)
C = np.zeros((2, 2))
D = np.diag((-3, -4))
print(np.block([[A, B], [C, D]]))

a = np.random.randint(1, 100, (3, 3))
print(a)
b = a.copy()
print(b)

data = "  1,  2,  3\n  4,  5, 67\n890,123,  4"
print(np.genfromtxt(StringIO(data), delimiter=",", autostrip=True))

array = "\n".join(str(i) for i in range(10))
print(np.genfromtxt(StringIO(array), skip_header=3, skip_footer=4))

data = "1 2 3\n4 5 6"
print(np.genfromtxt(StringIO(data), names="a, b, c", usecols=("a", "c")))

data = "arpit \n#a,b,c\n1,2,3\n4,5,6"
data_array = np.genfromtxt(StringIO(data), delimiter=",", skip_header=1, names=True)
print(data_array)
print(data_array.dtype)

data = StringIO("1 2 3\n 4 5 6")
data_array = np.genfromtxt(data, dtype=(int, float, int), defaultfmt="var_%02i")
print(data_array)
print(data_array.dtype)

a = 10 * np.random.rand(1, 9).reshape(3, 3)
print(a.dtype)
print(np.issubdtype(a.dtype, np.float64))
# print(np.issubdtype(a,float64))
print(np.power(100, 9, dtype=np.int32))
print(np.iinfo(np.int32))
print(np.iinfo(np.int64))
