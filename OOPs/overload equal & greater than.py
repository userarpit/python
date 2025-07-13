# Python program to overload
# a comparison operators

class A:
	def __init__(self, a):
		self.a = a

	def __gt__(self, other):
		if(self.a>other.a):
			return True
		else:
			return False
    
	def __eq__ (self,other):
		return self.a == other.a

ob1 = A(33)
ob2 = A(300)
if(ob1 == ob2):
	print("ob1 is equal to ob2")
elif (ob1>ob2):
	print("ob1 is greater than ob2")
else:
	print("ob2 is greater than ob1")