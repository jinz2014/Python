class counter:
  count = 0   # a class attribute
  def __init__(self):
    self.__class__.count += 1

if __name__ == '__main__':
  print(counter.count);
  c = counter()
  print(c.count);
  c = counter()
  print(counter.count);
