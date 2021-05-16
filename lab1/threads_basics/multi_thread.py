import threading
import time
import os


def worker():
	sum = 0
	for i in range(100_000_000):
		sum+=i

	print(f'sum = {sum}')


threads = []

# register all threads
for i in range(5):
	threads.append(threading.Thread(target=worker))
	print(f'thread {i} registered')


# start all threads
for tr in threads:
	tr.start()

# join all threads
for tr in threads:
	tr.join()

print("Worker did its job!")