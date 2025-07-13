
var1 = 'Hello World'


print(var1[:6] + "\sPython")

#escape character
print(r"\n example -> " + "Arpit \nKhandelwal")
print(r"\t example -> " + "Arpit \tKhandelwal")
print(r"\b example -> " + "Arpit \bKhandelwal")
print(r"\r example1 -> " + "Arpit \rKhandelwal")
print(r"\v example1 -> " + "Arpit \vKhandelwal")
print(r"\xnn example1 -> " + "Arpit \x61Khandelwal")

name = "Arpit"
print(f"My name is {name}")
print('My surname is {surname}'.format(surname='Khandelwal'))
print('My full name is {0} {1}'.format('Arpit','Khandelwal'))


print('{:<30}'.format('left aligned'))

print('{:*>30}'.format('right aligned'))

print('{:^30}'.format('centered'))

print('{:*^30}'.format('centered'))  # use '*' as a fill char

print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))
print('{:,}'.format(12345678))
width = 3
for element in range(1,10):
    print('{0:{width}b}'.format(element,width=width),end= ' ')
print()
str1 = 'Abcqdfe ryug'
print(str1.capitalize())
print(str1.center(12,'*'))
print(str1.find('df',2,8))
print(str1.startswith('ab'))
print(str1.islower())
print(max(str1))
print(min(str1))

print(str1.split())
str2='-234'
print(str2.zfill(6))
try:
    print(str1.index('dq',62,8))
except:
    print("Exception occur")
else:
    print("end")
finally:
    print("finally")

# join
strdash = "-"
seq = ("arpit","Khandelwal")
print(strdash.join(seq))

#maketrans
str3 = "abcdfkgjeabc"
input="abcde"
output="12345"
print(str3)
table = str3.maketrans(input,output)
print(table)
print(str3.translate(table))
 # type: ignoreprint(transtable)
