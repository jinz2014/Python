def make_counter(x):
  print ("enter make_counter")
  while True:
    yield x
    print ("count = {}".format(x))
    x = x + 1;

if __name__ == '__main__':
  counter = make_counter(2)      # return a generator
  print(counter.next())  # execution stops after yield x
  print
  print(counter.next())  # execution stops after yield x
  print
  print(counter.next())  # execution stops after yield x

