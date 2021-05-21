import threading
import time

def print_time(threadName, counter, delay):
	while counter:
		print("{:10s}: {:s}".format(threadName, time.ctime(time.time())))

		time.sleep(delay)

		counter -= 1


class myThread(threading.Thread):
	def __init__(self, name, delay):
		threading.Thread.__init__(self)
		self.name = name
		self.delay = delay

	def run(self):
		print(f"Starting {self.name}")
		print_time(self.name, 5, self.delay)
		print(f"\nExiting {self.name}")

# Create new threads
thread1 = myThread("Thread-1", delay=1)
thread2 = myThread("Thread-2", delay=2)

# Start new Threads
thread1.start()
thread2.start()

# Join new threads
thread1.join()
thread2.join()

print(f"\nExiting Main Thread")