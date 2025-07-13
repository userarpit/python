import re

p = re.compile('(\w+)\s+\1')

# findall() searches for the Regular Expression
# and return a list upon finding
s = "Python Python is awesome"
print(p.findall(s))
print(re.sub(r'(\w+)\s+\1', r'\1', s))