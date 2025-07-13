
file1 = open('../firstprogram.py', 'r')
print(file1.read(10))
file1.seek(0,2)
print(file1.tell())
for line in file1:
    print(line)

print(file1.mode)
print(file1.name)
print(file1.closed)

file1.close()
print(file1.closed)

file1 = open('secondfile.py','w')

file1.write("import math\n")
file1.write("print(math.factorial(5))\n")
file1.close()

file1 = open('secondfile.py','a')
file1.write("print(\"end\")")
file1.close()
