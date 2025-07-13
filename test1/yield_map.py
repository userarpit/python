import sys
sys.path.append('../function')

import division

# This is a placeholder for correct code for this message.
def table_2(my_list):
    """ yield table of 2 - each number one at a time"""
    for element in my_list:
        yield element

table_2_list = table_2(list(range(2,21,2)))
# print(table_2_list)

for number in table_2_list:
    print(number,sep="",end=" " )

print()
table_5 = map(lambda a:a*5,list(range(1,11)))
# for element in table_5:p
#     print(element,sep="",end=" ")

print(list(table_5))

print(list(map(pow,list(range(1,101)),[2] * 100)))
# print(math.pi)
print(division.div(3,4))
