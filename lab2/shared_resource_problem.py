import threading
import time


def worker():
	global counter

	for i in range(1_000_000):
		counter = counter + 1


counter = 0

# create some treads to count together:
thread_pool = []

for i in range(2):
	tr = threading.Thread(target=worker)
	thread_pool.append(tr)

	print(f"Counter before start of {tr.name}: {counter}")
	tr.start()


# wait for tread to finish:
for tr in thread_pool:
	tr.join()

print("Workers counted:", counter)