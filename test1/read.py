import os

fo = open("foo.txt","r+")
print(fo.name)
print("Closed or not : ", fo.closed)
print("Opening mode : ", fo.mode)
print(fo.read())

print(fo.tell())
fo.seek(0,0)
print(fo.readlines())
fo.seek(0,0)
print(fo.read(10))
fo.write("abc\n")
print(fo.tell())
print(type(fo))
print(fo.readlines())
#fo.truncate(21)
fo.seek(0,0)
print(fo.tell())
print(fo.readlines())  # read each line and return in list format
fo.close()

#os.rename("foo1.txt","foobar.txt")
#os.remove("foobar.txt")