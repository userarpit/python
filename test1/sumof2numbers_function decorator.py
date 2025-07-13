def summation(func):

    def inner(*args):
        print("Before calling function")

        total = func(*args)

        print("After calling function")
        return total

    return inner


@summation
def sum_of_two_number(a, b):
    print("inside the function")
    return a + b


# sum_of_two_number = summation(sum_of_two_number)
a, b = 2, 30
if __name__ == "__main__":
    print(sum_of_two_number(a, b))
    mylist = [1, 2, 3, 4]
    mylist.reverse()
    print(mylist)
    mylist.sort()
    print(mylist)
