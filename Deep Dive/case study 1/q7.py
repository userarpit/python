def fact(x):
	if x == 1:
		return 1
	else:
		return x * fact(x-1)

a = int(input("Enter a number "))
print(f"The factorial of the number {a} is {fact(a)}")

