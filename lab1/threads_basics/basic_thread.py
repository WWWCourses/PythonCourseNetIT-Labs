import threading
import time


def worker(x):
	tid = threading.currentThread().name;
	print(f"Work started in thread {tid}")
	time.sleep(2)
	print(f"Work ended in thread {tid}")


# create the tread
tr = threading.Thread(target=worker, args=(42,))

# start the thread:
print(f"Start Thread")
tr.start()

# wait until thread terminates:
# tr.join()

print("Main process end!")