from concurrent.futures import ThreadPoolExecutor
import time
import random
import threading

customer_queue = []
customer_available_condition = threading.Condition()


def now():
    return time.strftime("%H:%M:%S")


def serve_customer() -> None:
    while True:
        with customer_available_condition:
            while not customer_queue:
                print(f"{now()}: Teller is waiting for the customer")
                customer_available_condition.wait()

            customer = customer_queue.pop(0)

        process_time = random.randint(1, 10)
        print(
            f"{now()}: teller is serving {customer}. it will take {process_time} seconds"
        )
        time.sleep(process_time)

        print(f"{now()}: teller is finished with {customer}")


def add_customer_in_queue(name: str) -> None:
    with customer_available_condition:
        print(f"{now()}: {name} has arrived at the bank")
        customer_queue.append(name)

        customer_available_condition.notify()


def main() -> None:
    customer_names = [
        "Customer 1",
        "Customer 2",
        "Customer 3",
        "Customer 4",
        "Customer 5",
    ]

    with ThreadPoolExecutor(max_workers=6) as executor:
        executor.submit(serve_customer)
        for name in customer_names:
            time.sleep(random.randint(1, 10))
            executor.submit(add_customer_in_queue, name)
    
    # print("main end")


if __name__ == "__main__":
    main()
