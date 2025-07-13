def multiply(*args):
    """ multiply any number of arguments"""
    result = 1
    for element in args:
        result *= element
    return result


print(multiply(1, 2, 3))
print(multiply(1, 2, 30, 4, 5, 6))

""" my_list = [2,4,10,49,2]
print(multiply(my_list)) """

