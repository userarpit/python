# dog.py


class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return super().speak(sound)


class Bulldog(Dog):
    pass


gr = GoldenRetriever("Miles", 15)
print(gr.speak("bow"))
print(gr.speak())
print(isinstance(gr, GoldenRetriever))
print(isinstance(gr, Bulldog))
