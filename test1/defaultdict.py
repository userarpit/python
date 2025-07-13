from collections import defaultdict

def default():
    return "not present"

d = defaultdict(default)

d[1] = '1'
d[2] = '4'

print(d[3])
print(d[1])
print(d.__missing__(1))

# Python program to demonstrate
# defaultdict





# Defining a dict
e = defaultdict(list)

for i in range(5):
	e[i].append(i+2)

print("Dictionary with values as list:")
print(e)


# Python program to demonstrate
# defaultdict


from collections import defaultdict


# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:
	
	# The default value is 0
	# so there is no need to
	# enter the key first
	#d[i] += 1
    print(d[i])
	
print(d)
