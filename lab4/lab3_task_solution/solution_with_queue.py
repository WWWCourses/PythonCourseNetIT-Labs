"""ЗАДАЧА:
	Разгледайте дадения по-долу код и направете необходимите промени,
	така че след приключването на двата процеса променливата x да има стойност 20.

	Използвайте multiprocessing.Queue() за да обмените текущата стойност на x между процесите.
"""

import multiprocessing as mp

def increment(r):
	# global x
	x = queue.get()

	for _ in r:
		x+=1

	queue.put(x)
	print(f"x in {mp.current_process().name}: {x}")

if __name__ == "__main__":
	# x = 0
	queue = mp.Queue()
	queue.put(0)

	incr_count = 10

	# create and start 2 process which should increment a variable:
	pr1 = mp.Process(target=increment, args=(range(incr_count),))
	pr2 = mp.Process(target=increment, args=(range(incr_count),))
	pr1.start(); pr2.start()

	# wait processes to finish
	pr1.join();pr2.join()

	x = queue.get()
	print(f"x in {mp.current_process().name}: {x}")

	#Очакван  изход
	# x in Main Process: 20