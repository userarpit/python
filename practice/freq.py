from collections import Counter
from collections import defaultdict
import matplotlib.pyplot as plt
word = "mississippi"

counter = defaultdict(float)
# print(counter)
for letter in word:
    counter[letter] += 1

print(counter)

print(Counter(word))
sales = Counter(apple=10,orange=34)
monday_sales = Counter(apple=2,orange=10)
sales.update(monday_sales)
# print(sales)

for fruits in sales:
    print(fruits,sales[fruits])

print(sales.most_common(1))
x, y = zip(*sales.most_common())
plt.bar(x,y)
plt.show()