class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
		self.prev=None

class DoubleLinkedList:
	def __init__(self):
		self.head = None
		self.first = None

	def push(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			self.first = new_node
		else:
			temp = self.head
			temp.next = new_node
			new_node.prev = temp
			self.head = new_node

	def printDoubleLinkedList(self):
		temp = self.first
		while (temp):
			print(temp.data)
			temp = temp.next

	def find(self,afternodedata):
		temp = self.first

		node_found = False
		if temp is None:
			print("Double LinkedList is empty")
		
		while (temp and not node_found):
			# print(temp.next)
			if afternodedata == temp.data:
				afternode = temp
				node_found = True
			temp = temp.next
		
		if not node_found:
			afternode = None
		return afternode

	def insertafter(self, afternodedata, data):
		
		if self.head is None:
			print("Double Linked List is empty")

		afternode = self.find(afternodedata)
		if afternode is None:
			print(f"node with {afternodedata} is not found")
		else:
			new_node = Node(data)
			new_node.next = afternode.next
			afternode.next = new_node
			new_node.prev = afternode
			if new_node.next is not None:
				new_node.next.prev = new_node


dll = DoubleLinkedList()
dll.push(1)
dll.push(2)
dll.push(30)

dll.insertafter(1,3)
dll.push(40)
dll.printDoubleLinkedList()