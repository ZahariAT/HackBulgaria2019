import unittest

import collect_fractions

class TestSimplifyFraction(unittest.TestCase):
    def test_when_a_tuple_with_2_self_primes_is_given_then_return_same_tuple(self):
        expr = (1,2)
        expr_result = (1,2)
        self.assertEqual(collect_fractions.simplify_fraction(expr), expr_result)

    def test_when_a_tuple_with_2_numbers_with_GCD_different_than_1_is_given_then_return_tuple_with_the_numbers_divaded_by_GCD(self):
        expr = (2,8)
        expr_result = (1,4)
        self.assertEqual(collect_fractions.simplify_fraction(expr), expr_result)

    #def test_validate_fraction_object_is_a_tupel(self):
        #self.assertRaises(ValidationError, simplify_fraction, [1,1])
        #with self.assertRaises() as exc:
    #        simplify_fraction((1,2))
    #    self.assertEqual(' ', exc.exception)
    def test_if_given_value_is_list(self):
        list_with_a_no_tuple_value=[(1,2),2]
        self.assertRaises(ValueError, collect_fractions.collect_fractions ,list_with_a_no_tuple_value)

'''
    def test_when_a_tuple_(self):
        expr = [(2,8), ()]
        expr_result = (1,4)
        self.assertEqual(collect_fractions.collect_fractions(expr), expr_result)
'''
   
if __name__ == '__main__':
    unittest.main()