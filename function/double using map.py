from division import div as d
# Python program to demonstrate working
# of map.

# We double all numbers using map()
numbers = (1, 2, 3, 4)
results = map(lambda a: a + a, numbers)

# Does not Print the value
print(results)

# For Printing value

for result in results:
    print(result, end=" ")

print(d(2, 3))