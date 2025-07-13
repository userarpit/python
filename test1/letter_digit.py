Sentence = input("Enter Sentence - ")

alpha = 0
numeric = 0
for i in range(len(Sentence)):
	# print(Sentence[i])
	if (Sentence[i].isalpha()):
		alpha += 1
	elif (Sentence[i].isnumeric()):
		numeric += 1

print(f"Letters = {alpha}")
print(f"Numbers = {numeric}")