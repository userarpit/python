import re

pattern = re.compile('\d')

string1 = "andlj10 lkjd 34"
print(pattern.findall(string1))

pattern = re.compile('\d+')
print(pattern.findall(string1))