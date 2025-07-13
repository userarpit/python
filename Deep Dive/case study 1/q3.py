import time

localtime = time.localtime()

print(localtime) 
if 6 <= localtime.tm_hour < 18:
	print("it is day")
else:
	print("it is night")
