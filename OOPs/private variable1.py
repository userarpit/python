# A Python program to demonstrate that hidden
# members can be accessed outside a class
class MyClass:

	# Hidden member of MyClass
	__hiddenVariable = 10

# Driver code
myObject = MyClass()	

print(myObject._MyClass__hiddenVariable)
print(myObject._MyClass__hiddenVariable)