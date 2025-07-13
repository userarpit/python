# A Python program to demonstrate working
# of re.match().
import re
	
# a sample function that uses regular expressions
# to find month and day of a date.
def find_month_and_date(string):
		
	regex = r"([a-zA-Z]+) (\d+) ([2-9][\d]{3})"
	match = re.match(regex, string)
		
	if match == None:
		print ("Not a valid date")
		return
	
	print ("Given Data: %s" % (match.group()))
	print ("Month: %s" % (match.group(1)))
	print ("Day: %s" % (match.group(2)))
	print ("Year: %s" % (match.group(3)))
	
		
# Driver Code
find_month_and_date("June 24 3022")