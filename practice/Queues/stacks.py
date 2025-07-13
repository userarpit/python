from abstract_class import BaseDataStructure


class Stack(BaseDataStructure):
    def dequeue(self):
        return self._elements.pop()


stack = Stack("1st", "2nd", "3rd")

print(stack.dequeue())
