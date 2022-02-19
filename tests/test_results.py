"""Test dataframe processing functions from code/main.py

A module with "test_total_gps_message", "test_total_can_messages", "test_total_unique_can_messages", "test_total_run_time_of_data",
"test_avg_can_msg", "test_most_can_msg", "test_least_can_message"

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 18th, 2022
"""

import unittest
import pandas as pd
import sys
sys.path.append("/agi-coding-challenge/code")
sys.path.append("/agi-coding-challenge/data")

class TestResults(unittest.TestCase):

    df = pd.read_csv("/agi-coding-challenge/data/sample.csv")

    def test_total_gps_msg(self):
        pass