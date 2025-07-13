# Python code to demonstrate namedtuple()

from collections import namedtuple

# Declaring namedtuple()  kind of array
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
print(S[2])


Marks = namedtuple('Marks',['Eng','Maths','Science'])
s1 = Marks(20,40,60)

print(s1.Eng)

l1=[60,70,80]
s2=Marks._make(l1)
print(s2.Eng)
#print(S)

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(s2._asdict())

# Python code to demonstrate namedtuple() and
# _fields and _replace()

# importing "collections" for namedtuple()


# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)

# ._replace returns a new namedtuple, it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Manjeet'))
# original namedtuple
print(S)
