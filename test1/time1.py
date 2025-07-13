import time
from mylist import *

ticks = time.time()
print(ticks)

localtime = time.localtime(ticks)
print(localtime)


localtime = time.asctime(time.localtime(ticks))
print(localtime)

print(time.ctime())
print(time.localtime())
time.sleep(1)
print(time.localtime())

print(time.timezone)
print(time.tzname)
print(printinfo('Arpit',36))