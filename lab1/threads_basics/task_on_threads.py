import threading
import time


start = time.time()
def greet():
	time.sleep(1)
	print(f"Hello")


threads = []

# register 10 threads
for _ in range(100) :
	tr = threading.Thread(target=greet)
	threads.append(tr)


# start the threads
for tr in threads :
	tr.start()

# join the threads
for tr in threads:
	tr.join()


# Start 2 threads with greet function as target

end = time.time()

print(f"Time taken: {end-start}")
print(f"Main END!")