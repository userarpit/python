import re

password = input("Enter your password : ")
if re.fullmatch(r'[A-Za-z0-9$#@]{6,12}',password):
	print("Valid Password")
else:
	print("Invalid Password")