class A:
  def __init__(self, name, record):
    self.name = name
    self.record = record

  def copy(self):
    return self.__class__(self.name, self.record)

o1 = A('abc', {'a' : {'s':10, 'l':20}, 'b' : {'s':20, 'l':30}})
o2 = o1.copy()

o1.name = 'efg'

# expose a shallow copy
o1.record['a']['s'] = 20

print(o1.name, o1.record)
print(o2.name, o2.record)

