import math


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def is_perfect_bt(root):
    q = [root]
    flag = False
    count = 1
    depth = 0

    while len(q) > 0:
        if (count == math.pow(2, depth+1) - 1) and (not flag):
            depth += 1
        print(depth)
        curr = q.pop(0)
        if curr.left:
            if flag:
                return False
            q.append(curr.left)
            count += 1
        else:
            flag = True
        if curr.right:
            if flag:
                return False
            q.append(curr.right)
            count += 1
        else:
            flag = True

    if count == (math.pow(2, depth) - 1):
        return True


root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5) 
# root.right.left = Node(6)
# root.right.right = Node(7)

if is_perfect_bt(root):
    print("it is a perfect Tree")
else:
    print("it is not a perfect BT")
