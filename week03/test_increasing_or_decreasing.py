#there are a lot of different tests depending on the level of interactions
#Roza knows 25 deff tests
#unit tests are 1st level, only for function

import unittest

from week02_1 import increasing_or_decreasing

class TestIncreasingOrDecreasing(unittest.TestCase):
    def test_when_monotonously_increasing_list_is_passed_then_return_Up(self):  #normal to be so long
        self.assertEqual(increasing_or_decreasing([1,2,3,4,5]), 'Up!')

if __name__ == '__main__':
    unittest.main()