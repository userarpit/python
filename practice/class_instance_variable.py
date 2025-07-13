from collections import namedtuple
# class Dog:
#     num_legs = 4

#     def __init__(self, name):
#         self.name = name

# jack = Dog("Jack")
# jill = Dog("Jill")

# print(Dog.num_legs)
# print(jack.num_legs)

# print(jill.num_legs) 

# print(dir(jack))

# jack.num_legs = 6
# print(Dog.num_legs)
# print(jack.num_legs)

# print(jill.num_legs) 
# print(dir(jack))

Dog = namedtuple("Dog", "name num_legs", defaults=[4])
jack = Dog("Jack")
jill = Dog("Jill")
print(jack.num_legs)
jack = jack._replace(num_legs=6)
print(jack.num_legs)
print(jill.num_legs)
