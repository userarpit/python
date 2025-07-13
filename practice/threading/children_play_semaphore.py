from threading import Thread, Semaphore
import time
from typing import NoReturn


def enter_playground(index, semaphore):
    print("Child", index, "is waiting to enter the playground")
    with semaphore:
        print("Child", index, "is entering the playground")
        time.sleep(3)
        print("Child", index, "is leaving the playground")
        # semaphore.release()


def main() -> NoReturn:
    """
    This function manages the creation and execution of multiple threads
    where each thread represents a child entering and leaving the playground.
    
    Returns
    -------
    NoReturn
        This function does not return any value.
    """
    threads: list[Thread] = []
    semaphore: Semaphore = Semaphore(3)
    for i in range(1, 11):
        thread: Thread = Thread(target=enter_playground, args=(i, semaphore))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    # print("main end")


if __name__ == "__main__":
    main()
