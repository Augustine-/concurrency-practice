# Create a program that starts two threads. Each thread should print numbers from 1 to 5 with a short delay between each print.
# Use the 'threading' module.

import threading
from time import sleep

def count_to_five(thread_name):
    for t in range(1, 6):
        print(f"{thread_name}: count: {t}")
        sleep(1)

def main():
    t1 = threading.Thread(target=count_to_five, args=("Thread 1",))
    t2 = threading.Thread(target=count_to_five, args=("Thread 2",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

main()