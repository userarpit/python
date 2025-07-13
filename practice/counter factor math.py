from collections import Counter
import math
import factor
number = int(input("Enter a number - "))
factor_list = factor.find_factor(number)
print(factor_list)
prime_factors = Counter(factor_list)

print(math.prod(prime_factors.elements()))