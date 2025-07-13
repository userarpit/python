list1 = ['a','b','b','c','a','f','d','b','d']

sorted_list = sorted(list1)
print(sorted_list)

char = input("Enter character to search - ")
for i in range(len(list1)):
	if char == list1[i]:
		print(f"{char} found at {i}")