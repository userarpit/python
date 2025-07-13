word = input("Enter word separated by comma ").split(",")
sorted_list = sorted(word)
output=",".join(map(str,sorted_list))


print(output)
