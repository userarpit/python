class Queue:
	def __init__(self):
		self.queue = []

	def insert(self,data):
		self.queue.append(data)

	def remove(self):
		del self.queue[0]

	def printqueue(self):
		print(self.queue)

q = Queue()
q.insert(1)
q.insert(2)
q.insert(3)
q.insert(4)

q.remove()
q.remove()

q.insert(5)
q.insert(6)
q.printqueue()