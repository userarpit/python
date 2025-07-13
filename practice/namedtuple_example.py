from collections import namedtuple


Point = namedtuple("Point", (f for f in "xy"))
point = Point(y=2, x=4)
print(issubclass(Point, tuple))
print(point.x)
print(point)
print("*" * 100)

# name namedtuple

Person = namedtuple("Person", "name, children")
john = Person("John", ["Tina", "Jimmy"])

print(john.name)
print(john.children)
print(id(john.children))
john.children.append("Timmy")
print(john.children)
print(id(john.children))

print(hash(point))
# print(hash(john))
# john.name="abc"
# print(type(Person))
Developer = namedtuple(
    "Developer", "name level language", defaults=["Senior", "Python"]
)

d1 = Developer("Arpit")
print(d1)
print(d1.language)

d2 = Developer._make(["Shanaya", "Junior", "Python"])
print(d2)
print(d2._asdict())
# d2.level = "Super Senior" # error can't set attribute
d2 = d2._replace(name="Reyansh")  # return new instance
print(d2)

print(d2._fields)
print(d2._field_defaults)

Person_Detail = namedtuple("Person_Detail", "name age height")
Extended_Person_Detail = namedtuple(
    "Extended_Person_Detail", [*Person_Detail._fields, "weight"]
)

epd = Extended_Person_Detail("Jane", 26, 1.75, 67)

for field, value in zip(Extended_Person_Detail._fields, epd):
    print(f"{field} -> {value}")

for field, value in d2._asdict().items():
    print(f"{field} -> {value}")
