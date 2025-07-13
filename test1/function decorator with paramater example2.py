# Python code to illustrate
# Decorators with parameters in Python (Multi-level Decorators)

def decodecorator(data_type, message1, message2): #step 1; step 5
	def decorator(fun): #step 3 fun points to stringJoin; step 7 fun points to summation
		print(message1)
		def wrapper(*args, **kwargs):
			print(message2)
			if all([type(arg) == data_type for arg in args]):
				return fun(*args, **kwargs)
			return "Invalid Input"
		return wrapper # step 4 stringJoin points to wrapper; step 8 summation points to wrapper
	return decorator #step 2; step 6


@decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")
def string_join(*args):
	st = ''
	for i in args:
		st += i
	return st

#stringJoin = decodecorator(str, "Decorator for 'stringJoin'", "stringJoin started ...")(stringJoin)

@decodecorator(int, "Decorator for 'summation'\n", "summation started ...")
def summation(*args):
	summ = 0
	for arg in args:
		summ += arg
	return summ

#summation = decodecorator(int, "Decorator for 'summation'\n", "summation started ...")(summation)

print(string_join("I ", 'like ', "Geeks", 'for', "geeks"))
print()
print(summation(19, 2, 8, 533, 67, 981, 119))