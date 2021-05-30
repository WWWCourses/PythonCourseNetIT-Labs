import threading
import time
import random
from queue import Queue

BUF_SIZE = 3
q = Queue(BUF_SIZE)


class ProducerThread(threading.Thread):
  def __init__(self,name):
    threading.Thread.__init__(self)
    self.name = name

  def run(self):
    for _ in range(5):
      if not q.full():
        item = random.randint(1,10)
        q.put(item)
        print(f"Put item: {item} in queue")
        time.sleep(random.random())
    return

class ConsumerThread(threading.Thread):
  def __init__(self, name):
    threading.Thread.__init__(self)
    self.name = name

  def run(self):
    for _ in range(5):
      if not q.empty():
        item = q.get()
        print(f"Get item: {item} from queue")
        time.sleep(random.random())
    return

if __name__ == '__main__':
  p = ProducerThread(name='producer')
  c = ConsumerThread(name='consumer')

  p.start()
  time.sleep(2)
  c.start()
  # time.sleep(2)