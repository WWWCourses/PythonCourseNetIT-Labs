import threading
import time


def worker(x):
	# tid = threading.currentThread().name;
	print(f"Work started in thread and x = {x}")
	time.sleep(2)
	print(f"Work ended in thread")



# create thread
tr = threading.Thread(target=worker, name="tr1", args=(42,), daemon=None)

# start thread
tr.start()

tr.join()

print(f"Main process finished")