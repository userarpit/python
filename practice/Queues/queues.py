from abstract_class import BaseDataStructure


class Queue(BaseDataStructure):
    def dequeue(self):
        return self._elements.popleft()


if __name__ == "__main__":

    queue = Queue("1st", "2nd", "3rd")
# queue.enqueue("1st")
# queue.enqueue("2nd")
# queue.enqueue("3rd")

    print(len(queue))

    for element in queue:
        print(element)
