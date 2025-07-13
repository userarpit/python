import re

line = "nmjhArpitKhandelwal Arpat Kandelwal Khandelwal"

matchobj = re.sub("p[i,a]t","hole",line,1)
print(matchobj)
""" 
if matchobj:
    # print(matchobj.group())
    # print(matchobj.group(1))
    # print(matchobj.group(2))
    # print(matchobj.span(0))
    # print(matchobj.span(1))
    # print(matchobj.span(2))
else:
    print("no match") """