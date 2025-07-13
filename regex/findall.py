# return as list
import re

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

match = re.findall('\d+',string)
print(match)

# get all email address
text="lkasdnkldsn@lkasdi.com jadsihki akjsdhchd masterarpit@gmail.com"
new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", 
                           text, re.I))

print(new_emails)