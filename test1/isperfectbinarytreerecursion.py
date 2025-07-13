class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_depth(root):
    depth = 0
    # traverse through the left node to get the depth of the tree
    left_traverse = root
    while left_traverse.left:
        depth += 1
        left_traverse = left_traverse.left
    return depth


def is_perfect_binary_tree(root, depth, level=0):

    if root.left is None and root.right is None:
        return (depth == level)
    if root.left is None or root.right is None:
        return False

    return (is_perfect_binary_tree(root.left, depth, level + 1) and
            is_perfect_binary_tree(root.right, depth, level + 1))


if __name__ == '__main__':
    root = None
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    root.left.left = Node(40)
    root.left.right = Node(50)
    root.right.left = Node(60)
    root.right.right = Node(70)

    depth = find_depth(root)
    if is_perfect_binary_tree(root, depth):
        print("Tree is perfect")
    else:
        print("Tree is not perfect")