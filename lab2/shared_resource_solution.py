import threading
import time


def worker():
	global counter

	# start of critical section
	lock.acquire()
	for i in range(1_000_000):
		counter = counter + 1
		time.sleep(1)


	# end of critical section
	lock.release()

start = time.time()
counter = 0
lock = threading.Lock()

# create some treads to count together:
thread_pool = []

for i in range(5):
	tr = threading.Thread(target=worker)
	thread_pool.append(tr)

	print(f"Counter before start of {tr.name}: {counter}")
	tr.start()


# wait for tread to finish:
for tr in thread_pool:
	tr.join()

end = time.time()
print(f"Workers counted: {counter} for time: {end-start}")