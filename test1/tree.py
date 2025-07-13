class Node:
    """class Node"""

    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

    def insert(self, data):
        """create a Node with data and insert it in the tree

        Args:
            data (integer): data for which Node will be created
        """
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()

    def in_order_traversal(self, root):
        res = []
        if root:
            res = res + self.in_order_traversal(root.left)
            res.append(root.data)
            res = res + self.in_order_traversal(root.right)
        return res

    def pre_order_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        res = []
        if root:
            res = res + self.pre_order_traversal(root.left)
            res = res + self.pre_order_traversal(root.right)
            res.append(root.data)
        return res

    def find_val(self, lkvalue):
        if lkvalue < self.data:
            if self.left:
                return self.left.find_val(lkvalue)
            else:
                return f"Value {lkvalue} not found"
        elif lkvalue > self.data:
            if self.right:
                return self.right.find_val(lkvalue)
            else:
                return f"Value {lkvalue} not found"
        else:
            return f"Value {lkvalue} found"


# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
# root.print_tree()
print(root.in_order_traversal(root))
# print(root.data)
print(root.pre_order_traversal(root))
print(root.post_order_traversal((root)))

print(root.find_val(34))
print(root.find_val(6))
print(root.__doc__)
print(root.insert.__doc__)
