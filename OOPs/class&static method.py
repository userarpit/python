import datetime as date

class Person:
    name = ""
    age = 0

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __del__(self):
        print("Destuctor called for", self.name)

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.date.today().year - year)

    @staticmethod
    def is_adult(age):  
        return age > 18

person1 = Person('Arpit',36)
person2 = Person.from_birth_year('Shanaya',2013)

print(person1.age)
print(person2.age)

print(Person.is_adult(person2.age))

del person1
del person2

print("Good Bye")