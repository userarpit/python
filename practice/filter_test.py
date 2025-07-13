scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

over_75 = list(filter(lambda x: x > 75, scores))

print(over_75)

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda x: x == x[::-1], dromes))
print(palindromes)