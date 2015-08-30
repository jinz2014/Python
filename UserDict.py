class UserDict:
  def __init__(self, dict = None):
    self.data = {}
    if dict is not None: self.update(dict)

  def clear(self): self.data.clear()

  def update(self, dict):
    # do nothing if dict is None
    for (k, v) in dict.items():
      self.data[k] = v

  # this is a dict copy, not a class object copy
  def copy(self):
    #if self.__class__ is UserDict:
      # a shallow copy
      #return UserDict(self.data)

    # self may be some subclass of UserDict;
    # then other data attributes may be defined in the subclass
    import copy
    return copy.deepcopy(self.data)

  def keys(self): return self.data.keys()

  def items(self): return self.data.items()

  def values(self): return self.data.values()

  #def __getitem__(self, key): return self.data[key]

  def __setitem__(self, key, val): self.data[key] = val

  def __repr__(self): return repr(self.data)

  def __len__(self): return len(self.data)

  # del instance[key]
  def __delitem__(self, key): del self.data[key]

  # instance1 == instance2
  def __cmp__(self, dict):
    if isinstance(dict, UserDict):
      return cmp(self.data, dict.data)
    else:
      return cmp(self.data, dict)


if __name__ == '__main__':

  data = dict(name='jin', email='jinz@email.sc.edu', 
      degree_univ=dict(phd='usc', ms='shu'))

  a = UserDict(data);
  a['name'] = 'zheming'
  print(a, len(a))
  print(a.values())

  # b is of type dict
  b = a.copy()

  # UserDict must define __getitem__ and __setitem__ for it to work!
  b['name'] = 'tom'
  b['degree_univ']['phd'] = 'mit'
  print(b.values())

  # a shallow copy ?
  print(a.values())

  # update test
  profile = dict(name='jin', dob='02/01/1981', email='jinz@email.sc.edu')
  b.update(profile)
  print(b.values())

  profile = dict(name='tom')
  b.update(profile)
  print(b.values())


  profile = dict()
  b.update(profile)
  print(b.values())
