# for loop with else

for element in range(10):
    print(element,sep="",end=" ")
else:
    print("for finished")
print("Exit for")
"""
# while with else
 i = 0
while i < 10:
    print(i)
    i += 1
 else:
    print("while finished")
    
print("Exit while")
 """
my_list = [1,"Arpit","Khandelwal",2.3]

for element in my_list:
    print(element)

ctr = 1
while ctr < 10:
    print(ctr)
    ctr += 1

for i in range(1, 100):
    if i % 2 != 0:
        continue
    print(i,sep="",end=" ")
print()
try:
    print(1/0)
except ZeroDivisionError:
    print("divide by zero not allowed")
