import op as op

a = 34
b = 20

print(op.add(a,b))
print(op.sub(a,b))
print(op.mul(a,b))

print(op.truediv(a,b))
print(op.floordiv(a,b))
print(op.pow(a,b))
print(op.mod(a,b))

print()

print(op.le(a,b))
print(op.lt(a,b))
print(op.gt(a,b))
print(op.ge(a,b))
print(op.eq(a,b))
print(op.ne(a,b))

li = [1,2,3,4,5,7]

op.setitem(li,5,6)
print(li)

print(op.getitem(li,3))

print(op.getitem(li,slice(2,4)))

# Python code to demonstrate working of
# and_(), or_(), xor(), invert()

# importing op module
import op

# Initializing a and b

a = 1

b = 0

# using and_() to display bitwise and operation
print ("The bitwise and of a and b is : ",end="")
print (op.and_(a,b))

# using or_() to display bitwise or operation
print ("The bitwise or of a and b is : ",end="")
print (op.or_(a,b))

# using xor() to display bitwise exclusive or operation
print ("The bitwise xor of a and b is : ",end="")
print (op.xor(a,b))

# using invert() to invert value of a
op.invert(a)

# printing modified value
print ("The inverted value of a is : ",end="")
print (op.invert(a))
