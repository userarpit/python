import getpass
import pwinput 
while(True):
	password = pwinput.pwinput("Enter Password : ")
	if password == "Arpit@10":
		break
	else:
		print("Invalid password")

print("Please select from below option")

option =0
balance = 0
def check_balance():
	global balance
	print(f"Balance : {balance}")

def cash_credit():
	global balance
	amount = int(input("Enter Amount to credit : "))
	balance += amount

def cash_withdraw():
	global balance
	amount = int(input("enter Amount to Withdraw : "))
	balance -= amount

while(option != 4):
	print()
	print("1. Check Balance")
	print("2. Cash Credit")
	print("3. Cash Withdraw")
	print("4. Quit")

	try:
		option = int(input("option : "))
	except ValueError:
		pass

	match option:
		case 1:
			check_balance()
		case 2:
			cash_credit()
		case 3:
			cash_withdraw()
		case 4:
			continue
		case _:
			print("Please Enter valid option")


