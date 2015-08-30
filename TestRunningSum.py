import unittest
import sums

class TestRunningSum(unittest.TestCase):

  def test_all_negative(self) :
    arg = [-1, -5, -3, -4]
    exp = [-1, -6, -9, -13]
    sums.running_sum(arg)
    self.assertEqual(arg, exp, "The list contains only negative values")

  def test_all_mixed(self) :
    arg = [4, 0, 2, -5, 1]
    exp = [4, 4, 6, 1, 2]
    sums.running_sum(arg)
    self.assertEqual(arg, exp, "The list contains mixed values")

unittest.main()
