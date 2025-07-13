# from collections import namedtuple
from heapq import heappush, heappop
from dataclasses import dataclass
from itertools import count
from abstract_class import IterableMixin

@dataclass
class Message:
    event: str


class PriorityQueue(IterableMixin):
    def __init__(self):
        self._elements = []
        self._counter = count()

    # @staticmethod
    # def increase_count():
    #     return next(count())

    def enqueue_with_priority(self, priority, value):
        c = next(self._counter)
        # c = PriorityQueue.increase_count()
        # print(PriorityQueue.increase_count())
        print(c)
        element = (-priority, c, value)
        heappush(self._elements, element)

    
    def dequeue(self):
        return heappop(self._elements)[-1]


# Priority = namedtuple("Priority", )
CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1

messages = PriorityQueue()

wipers = Message("Windshield wipers turned on")
radio = Message("Radio station tuned in")
brake = Message("Brake pedal depressed")
hazard_lights = Message("Hazard lights turned on")

messages.enqueue_with_priority(IMPORTANT, wipers)
messages.enqueue_with_priority(NEUTRAL, radio)
messages.enqueue_with_priority(CRITICAL, brake)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

print(len(messages))
for message in messages:
    print(message)

# print(messages.dequeue())
# print(messages.dequeue())
# print(messages.dequeue())
# print(messages.dequeue())

