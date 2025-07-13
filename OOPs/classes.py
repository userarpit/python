class Dog:
    '''Dog class'''
    attr1 = "mammal"

    def __init__(self, name):
        self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

    def __del__(self):
        print("Destroy", self.name)

    def __str__(self):
        return f'called str {(self.name)}'


Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

print("Rodger is a {}".format(Dog.attr1))
print("Tommy is a {}".format(Dog.attr1))

Rodger.speak()
Tommy.speak()

print(type(Rodger))
print(Rodger.__class__)

print(hasattr(Rodger, 'name'))
print(hasattr(Rodger, 'age'))
print(Dog.__doc__)
print(Dog.__dict__)
print(Dog.__name__)
print(Dog.__bases__)
print(Rodger.name)
