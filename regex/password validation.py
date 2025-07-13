import re

'''
Should have at least one number.
Should have at least one uppercase and one lowercase character.
Should have at least one special symbol.
Should be between 6 to 20 characters long.
'''

password = input("Enter password ")

password_pattern = "^(?=.*[A-Z])(?=.*[a-z])(?=.*[\d])(?=.*[#?!@$%^&*-]).{4,10}$"
print(re.match(password_pattern, password)) # Returns None