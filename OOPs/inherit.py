class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age=age

    def display(self):
        print("Name -> {}".format(self.name))
        print("Age -> {}".format(self.age))

class Employee(Person):

    def __init__(self, name, age, eid, esal):
        self.eid = eid
        self.esal = esal
        Person.__init__(self,name, age)

    def display(self):
        super().display()
        print("Eid -> {}".format(self.eid))
        print("Esal -> {}".format(self.esal))

e = Employee("Arpit",36,12345,100000.00)
e.display()

print(issubclass(Employee,Person))
print(issubclass(Person,Employee))

print(isinstance(e,Person))