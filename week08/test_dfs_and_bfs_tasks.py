import unittest

import dfs_and_bfs_tasks

class TestTasks(unittest.TestCase):
    def test_deep_find_bfs_taking_nested_dict_and_finding_uptime_return_122(self):
        return_value = dfs_and_bfs_tasks.deep_find_bfs({'ah': {'uptime': 13002}, 'uptime': 122}, 'uptime')
        self.assertEqual(return_value, 122)

    def test_deep_find_bfs_taking_dict_with_any_iterable_value_except_str_and_finding_uptime_return_122(self):
        return_value = dfs_and_bfs_tasks.deep_find_bfs({'ah': [{'uptime': 13002}], 'uptime': 122}, 'uptime')
        self.assertEqual(return_value, 122)

    def test_deep_find_bfs_taking_dict_and_finding_non_existing_value_raise_Exceptien(self):
        with self.assertRaises(Exception):
            dfs_and_bfs_tasks.deep_find_bfs({'ah': [{'uptime': 13002}], 'uptime': 122}, 'downtime')
    
    def test_deep_find_dfs_taking_nested_dict_and_finding_uptime_return_13002(self):
        return_value = dfs_and_bfs_tasks.deep_find_dfs({'ah': {'uptime': 13002}, 'uptime': 122}, 'uptime')
        self.assertEqual(return_value, 13002)
    
    def test_deep_find_dfs_taking_dict_with_any_iterable_value_except_str_and_finding_uptime_return_13002(self):
        return_value = dfs_and_bfs_tasks.deep_find_dfs({'ah': [{'uptime': 13002}], 'uptime': 122}, 'uptime')
        self.assertEqual(return_value, 13002)

    def test_deep_find_dfs_taking_dict_and_finding_non_existing_value_raise_Exceptien(self):
        with self.assertRaises(Exception):
            dfs_and_bfs_tasks.deep_find_dfs({'ah': [{'uptime': 13002}], 'uptime': 122}, 'downtime')
    
    def test_deep_find_all_dfs_taking_nested_dict_and_finding_every_uptime_in_list(self):
        return_value = list(dfs_and_bfs_tasks.deep_find_all_dfs({'ah': {'uptime': 13002}, 'uptime': 122}, 'uptime'))
        self.assertEqual(return_value, [13002, 122])
    
    def test_deep_find_all_dfs_taking_dict_with_any_iterable_value_except_str_and_finding_every_uptime_in_a_list(self):
        return_value = list(dfs_and_bfs_tasks.deep_find_all_dfs({'ah': [{'uptime': 13002}], 'uptime': 122}, 'uptime'))
        self.assertEqual(return_value, [13002, 122])

    def test_deep_find_all_dfs_taking_dict_and_finding_non_existing_value_return_empty_list(self):
        return_value = list(dfs_and_bfs_tasks.deep_find_all_dfs({'ah': {'uptime': 13002}, 'uptime': 122}, 'showtime'))
        self.assertEqual(return_value, [])

    def test_deep_find_all_bfs_taking_nested_dict_and_finding_every_uptime_in_list(self):
        return_value = list(dfs_and_bfs_tasks.deep_find_all_bfs({'ah': {'uptime': 13002}, 'uptime': 122}, 'uptime'))
        self.assertEqual(return_value, [122, 13002])
    
    def test_deep_find_all_bfs_taking_dict_with_any_iterable_value_except_str_and_finding_every_uptime_in_a_list(self):
        return_value = list(dfs_and_bfs_tasks.deep_find_all_bfs({'ah': [{'uptime': 13002}], 'uptime': 122}, 'uptime'))
        self.assertEqual(return_value, [122, 13002])

    def test_deep_find_all_bfs_taking_dict_and_finding_non_existing_value_return_empty_list(self):
        return_value = list(dfs_and_bfs_tasks.deep_find_all_bfs({'ah': {'uptime': 13002}, 'uptime': 122}, 'showtime'))
        self.assertEqual(return_value, [])
    
if __name__=='__main__':
    unittest.main()