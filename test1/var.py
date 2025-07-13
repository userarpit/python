import mylist
import sys
import importlib
Money = 2000

def AddMoney():
# Uncomment the following line to fix the code:
        global Money
        Money = 23
        print(globals())
        return
        
print(Money)
AddMoney()
print(Money)

print(dir(mylist))
importlib.reload(mylist)