from abc import ABC, abstractmethod


class Animal(ABC):
    @property
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    @property
    def sound(self):
        print("bark")


d = Dog()
d.sound
