import multiprocessing
from time import sleep

"""
Write a program that uses the multiprocessing module to create two processes.
Each process should print numbers from 1 to 5 with a short delay between each print.
"""

def count_to_five(process_name):
    for n in range(1, 5):
        print(f"{process_name} printing: {n}...")
        sleep(2)
        print(f"{process_name} Done!")


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=count_to_five, args=["Process 1"])
    p2 = multiprocessing.Process(target=count_to_five, args=["Process 2"])

    p1.start()
    p2.start()
    p1.join()
    p2.join()
