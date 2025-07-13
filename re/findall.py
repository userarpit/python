import re

line = "nmjhArpit Khandelwal Arpit Khandelwal Khandelwal"

matchobj = re.findall(r"(.*)khan",line,re.IGNORECASE)
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