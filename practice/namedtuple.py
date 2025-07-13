from collections import namedtuple

Person = namedtuple('Person',['first_name','last_name'])
p = Person('Arpit','Khandelwal')
print(p)
p.first_name = 'g'