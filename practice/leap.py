year = int(input("Please enter year"))

if year % 4 == 0 and year % 400 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
