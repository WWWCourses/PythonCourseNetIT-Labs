import multiprocessing
import time
import os


def worker():
	sum = 0
	for i in range(100_000_000):
		sum+=i

	print(f'sum = {sum}')


Processs = []

# register all Processs
for i in range(5):
	Processs.append(multiprocessing.Process(target=worker))
	print(f'Process {i} registered')


# start all Processs
for pr in Processs:
	pr.start()

# join all Processs
for pr in Processs:
	pr.join()

print("Worker did its job!")