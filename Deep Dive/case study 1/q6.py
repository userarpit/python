number = list(range(2000,3201))

num_list = [value for value in number if (value % 7 ==0 and value % 5 !=0)]

print(num_list)
