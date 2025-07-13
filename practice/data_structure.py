from collections import OrderedDict, defaultdict
from collections import ChainMap

d = OrderedDict(one=1, two=2)
print(type(d['one']))
d['three'] = 3
print(d.keys())

dd = defaultdict(int)

name="arpit Khandelwal"

for letter in name:
    dd[letter] += 1

print(sorted(dd.items(), reverse=True, key=lambda x: x[1]))

print("*" * 100)
# chainmap

a = {}

