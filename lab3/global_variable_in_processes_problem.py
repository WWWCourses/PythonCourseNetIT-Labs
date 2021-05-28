import multiprocessing as mp

def increment(r):
  global x

  for _ in r:
    x+=1

  print(f'x in process: {mp.current_process().name}: {x}')


#   print(f"x in {mp.current_process().name}: {x}")


if __name__ == "__main__":
  x = 0

  incr_count = 1_000_000

#   increment(range(100))
#   increment(range(100))

  pr1 = mp.Process(target=increment, args=(range(incr_count),))
  pr2 = mp.Process(target=increment, args=(range(incr_count),))

  pr1.start();pr2.start();
  pr1.join();pr2.join();


  print(f"x in {mp.current_process().name}: {x}")