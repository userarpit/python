import threading
import time
import concurrent.futures as cf

def thread_function(name):
    print("Thread start", name)
    time.sleep(2)
    print("Thread end", name)


def main():
    with cf.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
        
if __name__ == "__main__":
    main()