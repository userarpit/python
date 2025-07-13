""" fo = open("foo.txt","r")
try:
        fo.write("Arpit")
except IOError:
        print("can't write! file is open in read only mode")
else:
        print("end")
finally:
        print("finally")
fo.close() """


def div(first_num, second_num):
    """ check for division by zero"""
    try:
        result = first_num / second_num
    except ZeroDivisionError:
        result = "can't divide by zero"
    except TypeError:
        result = "Handle type error"
    else:
        print("else")
    finally:
        print("finally")
        # return "finally"
    return result

print(div("5", 2))
print(a)
