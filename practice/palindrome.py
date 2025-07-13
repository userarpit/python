flag = False
check_string = input("Enter any string - ")
# length = len(check_string)
# for i in range(length):
#     if check_string[i] != check_string[length - i - 1]:
#         print("String is not palindome")
#         flag = False
#         break

if (check_string == check_string[::-1]):
    flag = True

if flag:
    print("string is palindrome")
