import unittest

class Test(unittest.TestCase):
  def above(self):
     actual = temperature.above_freezing(5.2)
     self.assertEqual(True, actual, "It is above freezing")
  def below(self):
     actual = temperature.above_freezing(-2)
     self.assertEqual(True, actual, "It is below freezing")
  def equal(self):
     actual = temperature.above_freezing(0)
     self.assertEqual(True, actual, "It is at freezing")

unittest.main()
