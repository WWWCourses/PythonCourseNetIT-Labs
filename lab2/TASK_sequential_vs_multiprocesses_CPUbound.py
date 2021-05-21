import threading
import time

max_range = 100_000_000
max_range_half = max_range//2

def worker(r):
	tid = threading.currentThread().name

	# do some hard and time consuming work:
	global result
	res = 0

	for i in r:
		res += i

	result += res
	print(f"Worker {tid} is working with {r}")


#################################################
# Sequential Processing:
#################################################
t = time.time()
result = 0

worker(range(max_range_half))
worker(range(max_range_half, max_range))

print(f"Sequential Processing result: ", result)
print(f"Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
t = time.time()
result = 0

tr1 = threading.Thread(target=worker, args=(range(max_range_half),))
tr2 = threading.Thread(target=worker, args=(range(max_range_half,max_range),))

tr1.start();tr2.start()
tr1.join(); tr2.join()

print(f"Multithreaded Processing result: ", result)
print(f"Multithreaded Processing took:",time.time() - t,"\n")