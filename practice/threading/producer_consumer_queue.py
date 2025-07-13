import concurrent.futures as cf
import time
import threading
import random
import queue


def producer(queue, event):
    while not event.is_set():
        message = random.randint(1, 10)
        queue.put(message)
        print(f"message produced {message}")

    print("producer received event exiting")


def consumer(queue, event):
    while not event.is_set() or not queue.empty():
        message = queue.get()
        print(f"message consumed {message}")

    print("consumer received event exiting.")


def main():
    pipeline = queue.Queue(maxsize=10)
    event = threading.Event()

    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

        time.sleep(0.1)
        event.set()


if __name__ == "__main__":
    main()
