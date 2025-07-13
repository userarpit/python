import re

p = re.compile('ab*')
print(p.findall("abbabjabbba"))

p = re.compile('ab+')
print(p.findall("abbabjabbba"))