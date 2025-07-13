import re

line = "njhgArpit Khandelwal Arpit Kha1delwalKhandelwalgjh khan"

matchobj = re.match(r'Arpit Khan(.*)',line)
print(matchobj)

if matchobj:
    print(matchobj.group())
    print(matchobj.group(1))
    print(matchobj.group(2))
    print(matchobj.span(0))
    print(matchobj.span(1))
    print(matchobj.span(2))
else:
    print("No match")