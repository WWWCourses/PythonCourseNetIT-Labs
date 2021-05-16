import threading
import time

def worker(x):
  tid = threading.currentThread().name

  # do some hard and time consuming work:
  time.sleep(2)
  print(f"Worker {tid} is working with {x}")


#################################################
# Sequential Processing:
#################################################
t = time.time()
worker(42)
worker(84)
print("Sequential Processing took:",time.time() - t,"\n")

#################################################
# Multithreaded Processing:
#################################################
tmulti = time.time()
tr1 = threading.Thread(target=worker, args=(42,))
tr2 = threading.Thread(target=worker, args=(82,))

tr1.start();tr2.start()
tr1.join(); tr2.join()
print("Multithreaded Processing took:",time.time() - tmulti)