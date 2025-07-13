def changelist(my_list1):
    my_list1.append("Arpit")
    return None


my_list = [1, 2, 3]
changelist(my_list)
print(my_list)
print(my_list[1:3])

new_list = [element * 2 for element in range(1, 11)]
print(new_list)

help(len)


# Function definition is here


def printinfo(name, age):
    """
    This prints a passed info into this function
    """
    print("Name: ", name)
    print("Age ", age)
    return None


# Now you can call printinfo function
printinfo(age=50, name="miki")
printinfo("Abc", 30)
