class Node:

	# constructor
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList():

	def __init__(self):
		self.head = None

	def printLinkedList(self):
		temp = self.head
		while (temp):
			print(temp.data)
			temp = temp.next

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head=new_node

	def find_node(self, data):
		temp = self.head
		while (temp):
			if temp.data == data:
				return temp
			temp = temp.next

	def insertafter(self,afternode,new_data):
		if afternode is None:
			print("The given previous node must be in LinkedList.")
			return

		new_node = Node(new_data)
		new_node.next = afternode.next
		afternode.next = new_node

	def append(self, new_data):
		temp = self.head
		new_node = Node(new_data)
		
		if temp is None:
			print(1)
			temp = new_node

		# traverse to the last node
		while (temp.next):
			temp = temp.next

		temp.next = new_node

if __name__ == "__main__":
	llist = LinkedList()

	first = Node(1)
	second = Node(2)
	third=Node(3)
	first.next = second
	second.next = third

	llist.head = first
#	llist.printLinkedList()

	
	# create new Node
	llist.push(0)
	llist.push(-1)
	llist.push(-2)
	llist.push(-3)
	# llist.printLinkedList()

	afternode = llist.find_node(0)
	llist.insertafter(afternode, -9)

	# llist.printLinkedList()
	llist.append(10)
	llist.append(11)
	llist.printLinkedList()