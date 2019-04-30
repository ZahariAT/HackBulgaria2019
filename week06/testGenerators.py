import unittest
import mock

import generators

class TestGenerators(unittest.TestCase):
    def test_whether_in_chain_list_and_set_arguments_are_given_and_return_value_is_converted_in_list(self):
        list_result = list(generators.chain([1, 2, 3], {3, 2}))
        expected_result = [1, 2, 3, 2, 3]
        self.assertEqual(list_result, expected_result)

    def test_wheter_in_chain_two_sets_are_given_and_return_value_is_converted_in_set(self):
        set_result = set(generators.chain({1, 2, 3}, {3, 2, 'i'}))
        expected_result = {1, 2, 3, 'i'}
        self.assertEqual(set_result, expected_result)

    def test_wheter_in_compress_when_list_and_mask_with_only_falses_are_given_and_return_empty_list(self):
        result = list(generators.compress(['ivo', '2'], [False, False]))
        expected_result = []
        self.assertEqual(result, expected_result)

'''
Something that looks promising and might help me/you

from generator import generator, generate
from mything import thingy

@generator
class MyTestCase(unittest.TestCase):

    @generate('a', 'b', 'cccc', 'ddd', 'eeeeee', 'f', 'g')
    def test_thingy(self, input):
        self.assertTrue(thingy(input))
'''

if __name__ == '__main__':
    #print({3,'i'})
    unittest.main()
