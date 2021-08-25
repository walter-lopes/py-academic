# Threading

# - A new thread is spanewd within the existing process
# Starting a thread is faster than starting a process
# Memory is shared between all threads
# Mutexes often necessary to control access to shared data
# One GIL for all threads

from threading import Thread
import os
import math
import time
import concurrent.futures

def do_something(number):
    print(f'do something {number}')
    time.sleep(1)


#Sample using single thread
start = time.perf_counter()

for i in range(10):
    do_something(i)

finish = time.perf_counter()

# Finished in 10.1 second(s)
print(f'Finished in {round(finish - start, 2)} second(s) using single thread')

#Sample using multi thread
start = time.perf_counter()

threads = []

for i in range(10):
    threads.append(Thread(target=do_something, args=[i]))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

finish = time.perf_counter()

# Finished in 1.01 second(s)
print(f'Finished in {round(finish - start, 2)} second(s) multi thread')


# Sample using multi thread with futures
start = time.perf_counter()
with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [i for i in range(10)]
    results = executor.map(do_something, secs)

finish = time.perf_counter()
print(f'Finished in {round(finish - start, 2)} second(s) multi thread with futures')



