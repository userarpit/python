from prime import is_prime

# number = int(input("Enter a number - "))
# # print(type(number))

def find_factor(number):
	factor_list = []
	for i in range (2,int(number/2)):
		if is_prime(i):
			temp = number
			while (temp % i == 0):
				factor_list.append(i)
				temp = int(temp / i)
	return factor_list