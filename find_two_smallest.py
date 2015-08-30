import time

# python 2.7.8 doesn't support perf_counter()
def time_it(find_func, list):
  t1 = time.perf_counter()
  find_func(list)
  t2 = time.perf_counter()
  return (t2 - t1) * 1000;

# find the smallest(1), remove it, find the smallest(2), add back the (1)
def find_two_smallest(L):
  """(list) -> tuple of (int, int)
  return a tuple of the indices of the two smallest values in list L
  """
  smallest = min(L)
  min1 = L.index(smallest)
  L.remove(smallest)

  next_smallest = min(L)
  min2 = L.index(next_smallest)

  #put smallest back into L
  L.insert(min1, smallest)

  # remember to increment the index!
  if min1 <= min2:
    min2 += 1

  return (min1, min2)

if __name__ == '__main__':
  L = [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
  t = find_two_smallest(L)
  print(t)
  elaps_time = time_it(find_two_smallest, L)
  # 0.00 ms is useless...
  print('"Find, remove, find" took {:.2f}ms.'.format(elaps_time)) 

