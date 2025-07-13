from collections import Counter

inventory = Counter([2,3,4,5,2,5,3,4,2,2,5,8])
print(inventory.most_common(1)[0])  
_, top_count = inventory.most_common(1)[0]
print([object for object, count in inventory.items() if count == top_count])