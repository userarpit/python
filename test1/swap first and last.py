# Python3 program to swap first
# and last element of a mylist

# Swap function
def swapmylist(mylist):
	
	start, *middle, end = mylist
	mylist = [end, *middle, start]
	
	return mylist
	
# Driver code
newmylist = [12, 35, 9, 56, 24]

print(swapmylist(newmylist))