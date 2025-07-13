for i in range (1000,3001):
	all_digit_even = True
	num = i
	if (num % 2 == 0):
		while(num != 0):
			last_digit = num % 10
			num = num // 10
			if (last_digit % 2 == 0):
				continue
			else:
				all_digit_even = False
				break

		if(all_digit_even):
			print(i)