import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

teller_barrier = threading.Barrier(3)

def now():
    return time.strftime("%H:%M:%S")

def prepare_for_work(name):
    print(f"{now()}: {name} is preparing their counter.")

    # Simulate the delay to prepare the counter
    time.sleep(random.randint(1, 10))
    print(f"{now()}: {name} has finished preparing.")

    # Wait for all tellers to finish preparing
    teller_barrier.wait()
    print(f"{now()}: {name} is now ready to serve customers.")

tellers = ["Teller 1", "Teller 2", "Teller 3"]

with ThreadPoolExecutor(max_workers=3) as executor:
    # for teller_name in tellers:
    #     executor.map(prepare_for_work, teller_name)
    executor.map(prepare_for_work, tellers)

print(f"{now()}: All tellers are ready to serve customers.")