# Python program to demonstrate private members
# of the parent class


class C(object):
	def __init__(self):
		self.c1 = 21

		# d is private instance variable
		self.__d = 10


class D(C):
	def __init__(self):
		self.e = 84
		C.__init__(self)


object1 = D()

# produces an error as d is private instance variable
print(object1._C__d)