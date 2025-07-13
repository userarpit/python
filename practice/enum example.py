from enum import Enum, auto
import string

class Day(Enum):
    def _generate_next_value(name, start, count, last_values):
        # print("call method")
        print(name, start, count, last_values)
        return name[0]
    MONDAY= auto()
    TUESDAY=auto()
    WEDNESDAY=3
    THURSDAY=4
    FRIDAY=5
    SATURDAY=6
    SUNDAY=7
print(list(Day))
class BaseTextEnum(Enum):
    def as_list(self):
        print(self)
        try:
            return list(self.value)
        except:
            return [str(self.value)]

class Alphabet(BaseTextEnum):
    LOWER_CASE=string.ascii_lowercase
    UPPER_CASE=string.ascii_uppercase

print(Alphabet.LOWER_CASE.as_list())
print(Alphabet.LOWER_CASE.value)
# a = "arpit"
# print(type(Alphabet.LOWER_CASE.value))