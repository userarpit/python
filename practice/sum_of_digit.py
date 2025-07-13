num = int(input("Enter Number "))

sum = 0

while num != 0:
    last_digit = num % 10
    sum += last_digit
    num = int(num / 10)
print(sum)
