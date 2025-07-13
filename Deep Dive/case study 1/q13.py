import sys
binary_input = input("Enter 4 digit binary data separated by , - ").split(",")

binary_input_to_integer = []
for i in binary_input:
	if (len(i) != 4):
		print("Length of each digit must be 4")
		sys.exit()
	else:
		binary_input_to_integer.append(int(i,2))

#print(binary_input_to_integer)

divisible_by_5 = [i for i in binary_input_to_integer if (i % 5 ==0)]
#print(divisible_by_5)
to_binary = []
for i in divisible_by_5:
	to_binary.append(format(i,"b"))

print(','.join(to_binary))
