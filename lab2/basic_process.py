import multiprocessing
import time


def worker(x):
	# tid = multiprocessing.currentThread().name;
	print(f"Work started in process and x = {x}")
	time.sleep(2)
	print(f"Work ended in process")

if __name__ == '__main__':
	# create process
	pr = multiprocessing.Process( target=worker, name="pr1", args=(42,) )

	# start process
	pr.start()

	pr.join()

	print(f"Main process finished")