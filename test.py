"""Test dataframe processing functions from code/utils.py

A module with "test_total_gps_message", "test_total_can_messages", "test_total_unique_can_messages", "test_total_run_time_of_data",
"test_avg_can_msg", "test_most_can_msg", "test_least_can_message"

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 18th, 2022
"""

import unittest # to perform unit test
import pandas as pd # to read sample.csv test file
from core.utils import (
    total_gps_msg, # to test total_gps_msg()
    total_can_msg, # to test total_can_msg
    total_unique_can_msg, # to test total_unique_can_msg
    total_runtime_of_data, #to test total_runtime_of_data
    avg_can_msg, #to test avg_can_msg
)

class TestResults(unittest.TestCase):

    df = pd.read_csv("data/sample.csv") 

    def test_total_gps_msg(self):
        """Test total_gps_msg() 
        Returns:
        _______
        OK: if test passes
        False: if test fails
        """
        expected = 3
        actual = total_gps_msg(self.df, 'gps_id')
        self.assertEqual(expected, actual)

    def test_total_can_msg(self):
        """Test total_can_msg() 
        Returns:
        _______
        OK: if test passes
        FAILED: if test fails
        """
        expected = 20
        actual = total_can_msg(self.df, 'message_id')
        self.assertEqual(expected, actual)

    def test_total_unique_can_msg(self):
        """Test total_unique_can_msg() 
        Returns:
        _______
        OK: if test passes
        FAILED: if test fails
        """
        expected = 1
        actual = total_unique_can_msg(self.df, 'dlc')
        self.assertEqual(expected, actual)

    def test_total_runtime_of_data(self):
        """Test total_runtime_of_data() 
        Returns:
        _______
        OK: if test passes
        FAILED: if test fails
        """
        expected = 2
        actual = total_runtime_of_data(self.df, 'ts')
        self.assertEqual(expected, actual)

    def test_avg_can_msg(self):
        """Test avg_can_msg
        Returns:
        _______
        OK: if test passes
        FAILED: if test fails
        """
        expected = 6.666666666666667
        actual = avg_can_msg(self.df, 'ts')
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()