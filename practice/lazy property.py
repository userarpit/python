# lazy_properties.py
import time

class LazyProperty:
    def __init__(self, function):
        print("init")
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        print("get")
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

    # def __set__(self,obj,value):
    #     print("set")
    #     pass

class DeepThought:
    @LazyProperty
    def meaning_of_life(self):
        print("meaning of life...waiting")
        time.sleep(3)
        return 42

my_deep_thought_instance = DeepThought()
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)
print(my_deep_thought_instance.meaning_of_life)