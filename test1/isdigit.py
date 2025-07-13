for i in range(100):
    a = chr(i)
#    if a.isdigit() == True:
#        print(a,end=" ")

    if a.isalpha() == True:
        print("{1} {0}".format(i,a))