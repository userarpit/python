# Python program to demonstrate
# ChainMap - dictionaries as object
	
	
from collections import ChainMap
	
	
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}
	
# Defining the chainmap
c = ChainMap(d1, d2, d3)
	
print(c)


# Please select Python 3 for running this code in IDE
# Python code to demonstrate ChainMap and
# reversed() and new_child()

# importing collections for ChainMap operations
import collections

# initializing dictionaries
dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 9, 'c' : 4 }
dic3 = { 'f' : 5 }

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap using map
print ("All the ChainMap contents are : ")
print (chain.maps)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap using map
print ("Displaying new ChainMap : ")
print (chain1.maps)

# displaying value associated with b before reversing
print ("Value associated with b before reversing is : ",end="")
print (chain1['b'])

# reversing the ChainMap
chain1.maps = reversed(chain1.maps)

# displaying value associated with b after reversing
print ("Value associated with b after reversing is : ",end="")
print (chain1['b'])
