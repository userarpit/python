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

	def DeletefromStart(self):	
		temp = self.head
		self.head = temp.next
		del temp


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

	def deletefromend(self):
		temp = self.head

		if temp is None:
			print("Linked List is already empty")
			return


		# traverse to the last node
		while (temp.next):
			# print(temp.data)
			if temp.next.next is None:
				last_node = temp.next
				temp.next = None
				del last_node
				return
			temp = temp.next

	def deleteafternode(self, deleteafter):
		temp = deleteafter
		deleteafter.next = deleteafter.next.next
		del temp

if __name__ == "__main__":
	llist = LinkedList()

	first = Node(1)
	second = Node(2)
	third=Node(3)
	fourth = Node(4)
	first.next = second
	second.next = third
	third.next = fourth

	llist.head = first
	# llist.printLinkedList()

	# delete from starting
	# llist.DeletefromStart()
	# llist.deletefromend()
	# llist.printLinkedList()

	
	
	# delete after certain node
	deleteafter = llist.find_node(2)
	llist.deleteafternode(deleteafter)
	llist.printLinkedList()