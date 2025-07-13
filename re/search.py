import re

line = "nmjhArpit Khandelwal Arpit Khandelwal ArPIT Khandelwal"
count = 0
matchobj = re.search(r'arpit Khan',line,re.IGNORECASE)
print(matchobj)
""" print(matchobj.start())
print(matchobj.end())
 """
# print(line)
while(matchobj!=None):
    count += 1
    line = line[matchobj.end():]
    matchobj = re.search(r'arpit Khan',line,re.IGNORECASE)
print(count)    
""" if matchobj:
    print(matchobj.group())
    print(matchobj.group(1))
    # print(matchobj.group(2))
    print(matchobj.span(0))
    print(matchobj.span(1))
    # print(matchobj.span(2))
else:
    print("no match") """