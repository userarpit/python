fo = open("foo.txt","w+")
print(fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
fo.write("Arpit Khandelwal\nit is great")
fo.close