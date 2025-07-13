string1 = input("Enter string - ")

even_string = ""
# print(list(string1))
for i in range(len(string1)):
	if i % 2 == 0:
		even_string = even_string + string1[i]

print(even_string)
