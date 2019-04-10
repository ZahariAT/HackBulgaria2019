import unittest 
import solution

class testPolynomialsDerivates(unittest.TestCase):
    def test_whether_a_single_variable_2_multiplyed_by_x_derived_is_displayed_correctly(self):
        single_var=solution.SingleArgument('2x')
        expected_result='2'
        self.assertEqual(single_var.derivate(),expected_result)
   
    def test_whether_a_single_variable_2_multi_by_x_pow_3_derived_is_displayed_correctly(self):
        single_var=solution.SingleArgument('2x^3')
        expected_result='6x^2'
        self.assertEqual(single_var.derivate(),expected_result)
  
    def test_whether_a_polynom_of_a_kind_2_multy_by_x_plus_3_multi_by_x_exponent_2_plus_5(self):
        polynom=solution.Polynom('2x+3x^2+5')
        expected_result='2+6x'
        self.assertEqual(polynom.polynom_derive(),expected_result)
  
    def test_whether_a_polynom_of_a_kind_4_multy_by_x_exponent_3_plus_2_multi_by_x_exponent_4_plus_5(self):
        polynom=solution.Polynom('4x^3+2x^4+5')
        expected_result='12x^2+8x^3'
        self.assertEqual(polynom.polynom_derive(),expected_result)
  
    def test_whether_a_single_variable_x_derived_is_displayed_correctly(self):
        polynom=solution.Polynom('x')
        expected_result='1'
        self.assertEqual(polynom.polynom_derive(),expected_resulsublt)
  
    def test_whether_a_single_variable_4_derived_is_displayed_correctly(self):
        polynom=solution.Polynom('4')
        expected_result='0'
        self.assertEqual(polynom.polynom_derive(),expected_result)

if __name__ == '__main__':
    unittest.main()