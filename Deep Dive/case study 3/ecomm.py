import csv
import re

def break_title_first_last_name(full_name):
	match = re.split(r"\s+", full_name)
	return match

def createOrder(cust,product_name,product_code):
	try:
		if cust.blacklisted == 1:
			raise CustomerNotAllowedException(cust)
	except Exception:
		return False
	else:
		return Order(product_name,product_code)

class Order:
	def __init__(self,product_name,product_code):
		self.product_name = product_name
		self.product_code = product_code

class CustomerNotAllowedException(Exception):
	def __init__(self,cust):
		self.cust=cust
		print(f"Customer is blacklisted : {self.cust.title} {self.cust.first} {self.cust.last}")

class Customer:
	def __init__(self,title,first,last,blacklisted):
		self.title = title
		self.first = first
		self.last = last
		self.blacklisted = blacklisted


with open('FairDealCustomerData.csv', mode ='r')as file:
	csvFile = csv.reader(file)
	cust = []
	for lines in csvFile:
		match = break_title_first_last_name(lines[1])
		cust.append(Customer(match[1],match[2],match[3],int(lines[2])))

order1 = createOrder(cust[1],"PC",102)
if order1:
	print(order1.product_name)
	print(order1.product_code)


