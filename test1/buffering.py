import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>', flush=True)
		time.sleep(1)
	else:
		print('Start')


# Print without newline in Python 3.x without using for loop

l=[1,2,3,4,5,6]

# using * symbol prints the list
# elements in a single line
print(*l)

#This code is contributed by anuragsingh1022