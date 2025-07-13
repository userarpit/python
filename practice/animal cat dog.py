# import ../test1

class Animal():
    def __init__(self,name):
        self.__name = name
    
    def sound(self,sound):
        print(f"{self.__name} sound {sound}")

class Dog(Animal):
    def __init__(self,name):
        # super().__init__(name)
        self.__name = name

    def sound(self,sound):
        print(f"{self.__name} sound {sound}")
    
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name)

    def sound(self,sound):
        print(f"{self._name} sound {sound}")
    
bull_dog = Dog("Bull Dog")
# meow_cat = Cat("Kitty")

bull_dog.sound("Bark")
print(vars(bull_dog))
# meow_cat.sound("meow")
animal = Animal("abc")
animal.sound("blow")
print(animal._Animal__name)

