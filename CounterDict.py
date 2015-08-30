from itertools import chain as _chain
from itertools import starmap as _starmap
from itertools import repeat as _repeat
from collections import Mapping

class Counter(dict):
  def __init__(*args, **kwargs):
    if not args:
      raise TypeError('__init__ of Counter boject '
                      'needs an argument')
    self = args[0];
    args = args[1:];  # shift 

    if len(args) > 1:
      raise TypeError('expects at most 1 arguments, got %d' %  len(args))


    super(Counter,self).__init__()

    # * unpack the arguments out of a list or tuple
    # ** unpack the arguments and make them keyword arguments
    self.update(*args, **kwargs)

  # if __repr__(self) is not implemented, then self is displayed 
  # as {} when instantiating a Counter object. Note self is
  # still {} though it has a string representation. 
  # So the value of self != the string repr of self
  # c1 = Counter('abc')  # self's value is {}
  # c1.update('abc')     # self's value is not {}
  def __repr__(self):
      if not self: return '%s()' % self.__class__.__name__
      #items = ', '.join(map('%r: %r'.__mod__, self.most_common()))
      #return '%s({%s})' % (self.__class__.__name__, items)
      return '%s({%s})' % (self.__class__.__name__, self.elements())

  def elements(self):
    # apply repeat function on each item 
    # chained inputs from a single iterabe

    # iteritems() 
    # Return an iterator over the dictionary's (key, value) pairs.     
    # items()
    # Return a copy of dictionary's list of (key, value) pairs.     
    return _chain.from_iterable(_starmap(_repeat, self.iteritems()))

  def update(*args, **kwargs):
    self = args[0]
    args = args[1:]
    iterable = args[0] if args else None

    if iterable is not None:
      if isinstance(iterable, Mapping):
        if self:
          # Only Mapping object supports iteritems()
          for e, c in iterable.iteritems():
            self[e] = self.get(e, 0) + c
        else:
          # dict update() accepts 
          # 1. another dictionary object 
          # 2. an iterable of key/value pairs (as tuples or other
          #    iterables of length two). 
          # 3. keyword arguments ( key/value pairs): 
          #    d.update(red=1, blue=2).
          super(Counter, self).update(iterable)
      else:
        for e in iterable:
          self[e] = self.get(e, 0) + 1

    if kwargs:
      self.update(kwargs)

  def __delitem__(self, item):
    if item in self:
      super(Counter, self).__delitem__(item)

  def __add__(self, other):
    if not isinstance(other, Counter):
      return NotImplemented

    result = Counter()

    for elem, cnt in self.items():
      new_cnt = cnt + other[elem]
      result[elem] = new_cnt

    for elem, cnt in other.items():
      if elem not in self:
        result[elem] = cnt

    return result

  def __reduce__(self):
    #print(type(self))
    print(dict(self))
    # a callable class, a tuple of arguments for the callable class
    return self.__class__ , (dict(self),)


if __name__ == '__main__':
  print('test case 1')
  # instantiation with string sequence
  c1 = Counter("abcba")
  print(c1['a']) #2

  # update with keyword 
  c1.update(a=4, b=2, c=0, d=-2)
  print(c1['b']) #4

  # update with dictionary 
  c1.update({'a':1, 'b':-1, 'c':1})
  print(c1['b']) #3

  # update with string sequence 
  c1.update('beef')
  print(c1['b']) #4

  print('test case 2')

  # instantiation with a Mapping
  c2 = Counter(a=4, b=2, c=0, d=-2)
  print(c2['b']) #2

  # update with dictionary 
  c2.update({'a':1, 'b':-1, 'c':1})
  print(c2['b']) #1

  # update with string sequence 
  c2.update('beef')
  print(c2['b']) #2

  # delete 
  del c2['b']
  #print(c2['b']) #KeyError
  c2.update('b')
  print(c2['b']) #1
  
  c3 = Counter(a=1, b = -2, c= -3)
  c4 = Counter(a=0, b = 2, c= 1, d=-1)
  c5 = c3 + c4
  assert(c5['a'] == 1)
  assert(c5['b'] == 0)
  assert(c5['c'] == -2)
  assert(c5['d'] == -1)
  #print(sorted(c1.elements()))

  c5.__reduce__()

'''
  # tuple
  c2 = Counter(('red', 'blue', 'red', 'green', 'blue', 'blue'))


  # copy
  c4 = Counter(c3)

  c3 = Counter(c2)
  print(c3.elements())
'''
