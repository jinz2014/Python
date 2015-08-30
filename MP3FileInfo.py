from FileInfo import FileInfo

'''
In the __init__ method, self is the newly created object. 
(MP3FileInfo doesn't define __init__, so it will call its 
ancestor to find the __init__, but self is an MP3File object)

In other class methods, it is the instance whose methods was called
'''

class MP3FileInfo(FileInfo):
  # private method
  def __parse(self, filename):
    print('parse a file', filename)

  def __setitem__(self, key, val):
    print('MP3FileInfo: call __setitem__')
    if  key == 'name' and val:
      self.__parse(val)
    # python searches and finds the class (UserDict) 
    # that defines __setitem__
    FileInfo.__setitem__(self, key, val)

if __name__ == '__main__':
  import sys
  print(FileInfo.__module__) # print out FileInfo
  print(sys.modules[FileInfo.__module__])

  # the name of the module in which the class is defined
  print(MP3FileInfo.__module__) # print out __main__
  print(sys.modules[MP3FileInfo.__module__])

  # 1. call FileInfo's __init__
  # 2  FileInfo's __init__ then calls self['name'] = filename. 
  #    Notice self is fi, an MP3FileInfo class instance!
  # 
  # 3  which calls MP3FileInfo's __setitem__
  # parse a file 'mp3 file information'!
  fi = MP3FileInfo('mp3 file information')
  print(fi.data)

  # parse a file test.mp3
  fi['name'] = 'test.mp3'
  print(fi.data)

  # the error message is misleading..
  fi.__parse('private function')
