import random
import threading
import concurrent.futures as cf
# import time


class Pipeline:
    SENTINLE = 999

    def __init__(self) -> None:
        self._message = 0
        self.producer_lock = threading.Lock()
        self.consumer_lock = threading.Lock()
        self.consumer_lock.acquire()

    def get_message(self) -> None:
        self.consumer_lock.acquire()
        message = self._message
        # time.sleep(2)
        print(f"consume {message}")
        self.producer_lock.release()
        return message

    def set_message(self, message: int) -> None:
        self.producer_lock.acquire()
        self._message = message
        # time.sleep(2)
        print(f"produce {message}")
        self.consumer_lock.release()


def producer(pipeline: Pipeline) -> None:
    for _ in range(1, 10):
        message = random.randint(1, 10)
        pipeline.set_message(message)
        print(f"producer got message {message} iteration {_}")

    pipeline.set_message(Pipeline.SENTINLE)


def consumer(pipeline: Pipeline) -> None:
    message = 0
    while message != Pipeline.SENTINLE:
        message = pipeline.get_message()
        if message != Pipeline.SENTINLE:
            print(f"Consumer storing message {message}")


def main():
    pipeline = Pipeline()

    with cf.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline)
        executor.submit(consumer, pipeline)


if __name__ == "__main__":
    main()
