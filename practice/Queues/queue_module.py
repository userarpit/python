from queue import Queue, LifoQueue, PriorityQueue
import queue

q = Queue()

q.put("a")
q.put("b")
q.put("c")
# q.get()

try:
    while (not q.empty()):
        print(q.get_nowait())
except queue.Empty:
    print("Queue is Empty")

lq = LifoQueue()

lq.put("a")
lq.put("b")
lq.put("c")

while(not lq.empty()):
    print(lq.get())


pq = PriorityQueue()

pq.put((1, 'Cherry'))
pq.put((3, 'Banana'))
pq.put((2, 'Apple'))
pq.put((2, 'Kiwi'))
print("*" * 100)
while (not pq.empty()):
    print(pq.get()[1])