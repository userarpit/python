string1 = input("Enter String - ")
dict1 = {"upper":0,"lower":0}
for i in string1:
	if i.isupper():
		dict1["upper"] += 1
	elif i.islower():
		dict1["lower"] += 1

print(f"UPPER CASE : {dict1['upper']}")
print(f"lower case : {dict1['lower']}")
