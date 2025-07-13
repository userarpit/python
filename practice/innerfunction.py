def speak(text):
    def whisper():
        return text.upper()
    return whisper

print(speak("hello World")())

# print(whisper("Tto upper"))

class Adder:
    def __init__(self,x):
        self.x = x
    
    def __call__(self,y):
        return self.x + y
    
plus_3 = Adder(3)
print(plus_3.__call__(4))