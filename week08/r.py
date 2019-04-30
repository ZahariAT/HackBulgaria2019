import unittest

import dfs_and_bfs_tasks

class TestTasks(unittest.TestCase):
    def test_deep_find_dfs_taking_example_and_finding_uptime_return_13002(self):
        return_value = dfs_and_bfs_tasks.deep_find_dfs({'uptime': 13002}, 'uptime')
        self.assertEqual(return_value, 13002)