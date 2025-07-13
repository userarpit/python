'''
Function can be assigned to a variable i.e they can be referenced.
Function can be passed as an argument to another function.
Function can be returned from a function.
'''

# code for testing decorator chaining
def decor1(func): # func points to inner of decor
	def inner():
		x = func() # inner of decor is called, x = 20
		return x * x # 400 is returned
	return inner # inner is returned and num is pointing to inner at line #3

def decor(func): # func point to num
	def inner():
		x = func() # actual num is called, and return 10; x = 10
		return 2 * x # 20 is returned
	return inner # inner is returned and passed as argument to decor1

@decor1
@decor
def num():
	return 5

# num = decor1(decor(num)) -> num = inner at line number 3

print(num()) # call inner at line number 3; 400 is print