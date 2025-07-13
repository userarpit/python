''''''
from collections import OrderedDict

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od.keys())

od.pop('b')

od['b'] = 4

print(od.keys())

# normal dictionary
d = dict()
d['a'] = 1
d['b'] = 1
d['c'] = 1
d['d'] = 1

print(d)