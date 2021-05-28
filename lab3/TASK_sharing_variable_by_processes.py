import multiprocessing as mp

def increment(r):
	global x

	for _ in r:
		x+=1

	# write x in queue:
	queue.put(x)

	# print(f"x in {mp.current_process().name}: {x}")

if __name__ == "__main__":
	x = 0

	queue = mp.Queue();

	incr_count = 10

	pr1 = mp.Process(target=increment, args=(range(incr_count),))
	pr2 = mp.Process(target=increment, args=(range(incr_count),))

	pr1.start()
	x = queue.get()
	print(f'x from gueue: {x}')
	pr2.start()

	pr1.join()
	pr2.join()

	print(f"x in {mp.current_process().name}: {x}")


	#OUTPUT
	# x in Main Process: 20