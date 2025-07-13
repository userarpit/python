import re
import datetime

def check_characters_only(input_string):
  """
  Checks if a string contains only characters (letters).

  Args:
    input_string: The string to check.

  Returns:
    True if the string contains only characters, False otherwise.
  """
  pattern = r"^[a-zA-Z]+$"
  if re.match(pattern, input_string):
    return True
  else:
    return False
   
def gender_selected(radio_button_selected_option):
   
   if radio_button_selected_option == '':
        return False
   else:
        return True

def date_incorrect(date):
    day, month, year = date.split()

    day = int(day)
    year=int(year)

    days_30_month_list = ["April","June","September","November"]

    if month in days_30_month_list:
        if day == 31:
            return True
    
    if month == 'February' and day > 29:
        return True
    
    if month == 'February' and day == 29:
        if year % 4 !=0 or (year % 4 == 0 and year % 400 == 0):
            return True   

def phone_number_not_correct(phone_number):
    validate_phone_number_pattern = "^[1-9][0-9]{9}$"
    if re.match(validate_phone_number_pattern, phone_number):
        return False # Returns Match object
    return True

def any_field_missing(called_from, *args):
    missing_list = []    
    missing = False
    if not check_characters_only(args[0]):
        missing_list.append("First Name must contain only Alphabets and it should not be spaces!")
        missing = True
    if not check_characters_only(args[1]):
        missing_list.append("Last Name must contain only Alphabets and it should not be spaces!")
        missing = True
    if not gender_selected(args[2]):
        missing_list.append("Gender not selected!!")
        missing = True
    if len(args[3].split()) == 0 | len(args[3].split()) != 3 :
        missing_list.append("Date of Birth missing!")
        missing = True
    if called_from == 'Search':
        return missing_list, missing
    if args[4] == '':
        missing_list.append("Weight of the Child during birth missing!")
        missing = True
    if args[5] == '':
        missing_list.append("Length of the Child during birth missing!")
        missing = True
    if args[6] == '':
        missing_list.append("Child's mother name missing!")
        missing = True
    if args[7] == '':
        missing_list.append("Child's father name missing!")
        missing = True
    if args[8] == '':
        missing_list.append("phone number of the parent missing!")
        missing = True

    return missing_list, missing