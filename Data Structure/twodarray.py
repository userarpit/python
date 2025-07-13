# from array import *

T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

def print2darray(t):
	for r in t:
		for d in r:
			print(d,end=" ")
		print()	
# print(T[1])

# print(T[1][2])

print2darray(T)
print()
T.insert(2,[1,2,3,4])
print2darray(T)
print()
T[3] = [0,0,0,0]
print2darray(T)
print()
del T[2]
print2darray(T)