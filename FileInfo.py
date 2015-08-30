from UserDict import UserDict

class FileInfo(UserDict):
  ''' store file metadata '''

  def __init__(self, filename):
    print('FileInfo.py: call __init__ by the object of class', 
        self.__class__)
    # must use self to call an ancester method
    UserDict.__init__(self)

    # this is translated to the function
    # __setitem__(self, 'name', filename). 
    self['name'] = filename

  # Note Python doesn't check if you override __setitem__ properly
  # (i.e. when you don't call the base method)
  def __setitem__(self, key, val):
    print('FileInfo: call __setitem__')
    UserDict.__setitem__(self, key, val)


if __name__ == '__main__':
  fi = FileInfo('file information')
  #  a ref to the class that self is an instance of
  print(fi.__class__)
  print(fi.data)
  print(fi)
