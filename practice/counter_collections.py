from collections import Counter

c = Counter("abcdabcdabchfg")
print(c)
c.update({"sword":1})
print(c)

c.update(list("khandelwal"))
print(sorted(c.items(), reverse=True, key=lambda x: x[1]))
print(sorted(c.elements()))
print(len(c))
print(sum(c.values()))
print(c.most_common(5))
print(c.total())
# c.clear()
print(c)
print(dict(c))
    