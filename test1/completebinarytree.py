class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_tree(nums):
    if not nums:
        return None

    root = Node(nums[0])
    q = [root]
    i = 1
    # print(len(nums))
    while i < len(nums):
        # print(i, nums[i])
        curr = q.pop(0)
        if i < len(nums):
            curr.left = Node(nums[i])
            q.append(curr.left)
            i += 1
        
        if i < len(nums):
            curr.right = Node(nums[i])
            q.append(curr.right)
            i += 1
            
    return root

def print_tree(root):
    res = []
    if root:
        res = res + print_tree(root.left)
        res.append(root.data)
        res = res + print_tree(root.right)
    return res

nums = [1, 2, 3, 4, 5, 6, 6, 6, 6]
root = build_tree(nums)
print(print_tree(root))
