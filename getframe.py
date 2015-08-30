import sys

# not finished
def test():
  result.__module = sys._getframe(1).f_globals.get('__name__', '__main__')
  return result

print(test());
