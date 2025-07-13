from enum import Enum, auto, unique

@unique
class CardinalDirection(Enum):
    def _generate_next_value_(name, start, count, last_values):
        print(name,start,count,last_values)
        return name[0]
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

print(list(CardinalDirection))
print(CardinalDirection.NORTH.value)
# print(type(CardinalDirection.__members__))
print(CardinalDirection.NORTH == CardinalDirection.SOUTH)
for direction in CardinalDirection:
    print(direction.value)
print(CardinalDirection.NORTH in CardinalDirection)
print(sorted(CardinalDirection,key=lambda card: card.value))

class Day(Enum):
    def _generate_next_value(name, start, count, last_values):
        # print("call method")
        print(name, start, count, last_values)
        return name[0]
    MONDAY = auto()
    TUESDAY = auto()

print(list(Day))