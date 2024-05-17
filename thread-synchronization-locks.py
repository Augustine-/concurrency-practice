import threading
import time

"""
Write a program that uses a shared counter variable. Create multiple threads that increment this counter.
Use locks to ensure that the counter is updated correctly without race conditions.
"""

count = 0
lock = threading.Lock()

def counter(n):
    global count
    global lock
    while True:
        with lock:
            if count > 21:
                break
            print(f"thread {n} incrementing {count} by {n}")
            count += n
        time.sleep(1)


if __name__ == '__main__':
    start = time.perf_counter()
    threads = []

    for i in range(1, 3):
        t = threading.Thread(target=counter, args=[i])
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"final count: {count} reached in {round(end - start, 2)} seconds.")
