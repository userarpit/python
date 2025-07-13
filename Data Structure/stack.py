class Stack:
	def __init__(self):
		self.stack = []

	def push(self,data):
		self.stack.append(data)

	def pop(self):
		del self.stack[-1]

	def printstack(self):
		print(self.stack)

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

s.pop()
s.pop()
s.push(5)
s.push(6)

s.printstack()