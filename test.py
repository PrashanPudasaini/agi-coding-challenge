"""Test dataframe processing functions from code/utils.py

A module with "test_total_gps_message", "test_total_can_messages", "test_total_unique_can_messages", "test_total_run_time_of_data",
"test_avg_can_msg", "test_most_can_msg", "test_least_can_message"

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 18th, 2022
"""

import unittest # to perform unit test
import pandas as pd # to read sample.csv test file
from core.utils import total_gps_msg # to test total_gps_msg()

class TestResults(unittest.TestCase):

    df = pd.read_csv("data/sample.csv") 
    gps_id = 'gps_id'

    def test_total_gps_msg(self):
        """Test total_gps_msg() 
        Returns:
        _______
        True: if test passes
        False: if test fails
        """
        expected = 3
        actual = total_gps_msg(self.df, self.gps_id)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()