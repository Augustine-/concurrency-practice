import queue
import threading
import random
from time import sleep

"""
Implement a simple Producer-Consumer problem using the queue module and the threading module.

The producer thread should add items to a queue, and the consumer thread should remove items from the queue and process them.
"""

# Create a shared queue
shared_queue = queue.Queue(maxsize=10)

def consumer():
    while True:
        print("Consuming...")
        fib = shared_queue.get()
        fib += shared_queue.get()
        sleep(1)
        print(f"Consumed {fib}!")

def producer():
    while True:
        print("Producing two random ints...")
        shared_queue.put(random.randint(1, 100))
        shared_queue.put(random.randint(1, 100))
        sleep(1)
        print("Done!")

if __name__ == '__main__':
    consumer_thread = threading.Thread(target=consumer, daemon=True)
    producer_thread = threading.Thread(target=producer, daemon=True)

    consumer_thread.start()
    producer_thread.start()

    try:
        sleep(10)
    except KeyboardInterrupt:
        print("Stopping threads...")
    finally:
        consumer_thread.join(timeout=1)
        producer_thread.join(timeout=1)