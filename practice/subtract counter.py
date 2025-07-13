from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt

inventory = Counter(apple=10,orange=34)
monday_sales = Counter(apple=2,orange=-10)
inventory.subtract(monday_sales)
# print(sales)

for fruits,count in inventory.items():
    print(fruits,count)
print(+inventory)
print(-monday_sales)