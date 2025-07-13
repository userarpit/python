class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_complete_bt(root):
    q = [root]
    flag = False
    while len(q) > 0:
        curr = q.pop(0)
        if curr.left:
            if flag:
                return False
            q.append(curr.left)
        else:
            flag = True
        if curr.right:
            if flag:
                return False
            q.append(curr.right)
        else:
            flag = True

    return True


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(6)


if is_complete_bt(root):
    print("it is a complete binary Tree")
else:
    print("it is not complete BT")
