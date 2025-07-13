i = 100
print(hex(i))
#hex
s = "0x11"
print(int(s,16))

#oct
s = "76253"
print(int(s,8))

#float
print(float(123))

#complex
print(complex(4,4))

#dictionary
mylist = ['a',2,'b',4]
it = iter(mylist) 
print(dict(zip(it,it)))
#    print(i,j)
