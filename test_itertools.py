
from itertools import chain, starmap, repeat

def elements(self):
  # make an iterator that applys repeat function on each item 
  # chained multiple iterators into a single iterator
  return chain.from_iterable(starmap(repeat, self.iteritems()))


# iteritems() is a dict method
s = dict(b=2, a=2, d=3, c=1)

# ['a', 'a', 'b', 'b', 'c', 'd', 'd', 'd']
print(sorted(elements(s)))
