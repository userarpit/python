x,y = list(map(int,input("Enter 2 numbers seprated by comma - ").split(",")))

output = []
for i in range(x):
	internal = []
	for j in range(y):
		internal.append(i*j)
	output.append(internal)

print(output)

