import unittest
from rpn import rpn_calculate

class TestReversedPolishNotation(unittest.TestCase):
    def test_when_single_digit_is_passed_then_return_the_same_digit(self):
        expr = '45'
        expected_result = 45
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_two_numbers_are_passed_then_return_sum_of_them(self):
        expr = '4 8 +'
        expected_result = 12
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_two_numbers_are_passed_then_return_sub_of_them(self):
        expr = '4 8 -'
        expected_result = -4
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_a_lot_of_numbers_are_passed_then_return_their_evaluation(self):
        expr = '3 5 8 * 7 + *'
        expected_result = 141
        self.assertEqual(rpn_calculate(expr), expected_result)

    def test_when_a_number_is_add_and_return_its_sqrt(self):
        expr = '9 SQRT'
        expected_result = 3
        self.assertEqual(rpn_calculate(expr), expected_result)



if __name__ == '__main__':
    unittest.main()