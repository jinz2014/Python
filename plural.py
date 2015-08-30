import unittest
import re

def plural(n):
  if re.search('[sxz]$', n):
    return re.sub('$', 'es', n)
  elif re.search('[^aeioudgkptr]h$', n):
    return re.sub('$', 'es', n)
  elif re.search('[^aeiou]y$', n):
    return re.sub('y$', 'ies', n)
  else:
    return n + 's'

class Test(unittest.TestCase):
  def setUp(self):
    self.nouns = {'bus': 'buses', 
                  'cough': 'coughs',
                  'fly': 'flies'}

  def test_plurals(self):
    for n, p in self.nouns.items():
      self.assertEqual(plural(n), p)

if __name__ == '__main__':
  unittest.main()


