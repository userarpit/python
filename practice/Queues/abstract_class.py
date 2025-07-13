from abc import ABC, abstractmethod
from collections import deque


class DataStructure(ABC):

    @abstractmethod
    def enqueue(self):
        pass


    @abstractmethod
    def dequeue(self):
        pass


class IterableMixin:
    def __len__(self):
        return len(self._elements)

    def __iter__(self):
        while len(self) > 0:
            yield self.dequeue()


class BaseDataStructure(DataStructure, IterableMixin):
    
    def __init__(self, *elements):
        self._elements = deque(elements)

    def enqueue(self, element):
        self._elements.append(element)

    @abstractmethod
    def dequeue(self):
        pass
