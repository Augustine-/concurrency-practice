# Write a program that uses a thread pool to calculate the square of numbers from 1 to 10.
# Use concurrent.futures.ThreadPoolExecutor.

import concurrent.futures
from time import sleep

numbers = list(range(1,11))

def calculate_square(n):
    print(f"Thread {n} calculating square of {n}...")
    sleep(3)
    print(f"{n} Done!")
    return n*n

with concurrent.futures.ThreadPoolExecutor() as exec:
    futures = {exec.submit(calculate_square, n): n for n in numbers}

for f in futures:
    print(f.result())