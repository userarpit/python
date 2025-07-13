from collections import namedtuple
from datetime import date

BasePerson = namedtuple("BasePerson", "name birthdate country", defaults=['Canada'])

class Person(BasePerson):
    """A namedtuple subclass to hold a person's data."""
    __slots__ = []

    def __repr__(self):
        return f"{self.name} is {self.age} years old"

    @property
    def age(self):
        return (date.today() - self.birthdate).days // 365


print(Person.__doc__)

jane = Person("Jane", date(1986, 5, 10))
print(jane.age)
print(dir(jane))