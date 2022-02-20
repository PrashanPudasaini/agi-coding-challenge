"""Entry point to the application. Run "python main.py"

A module with "main" that prints to stdout total gps message, total unique CAN messages, total CAN messages, total run time of data, 
average CAN message per second and per gps message, first timestamp with most most CAN messages, first timestamp
with least CAN messages

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 19th, 2022
"""

import pandas as pd #to read csv file
from datetime import datetime # to measure app performance
from core.utils import (
    total_gps_msg, # to print total gps message from the gas_can_data.csv file
    total_can_msg, # to print total can messages from the gas_can_data.csv file
    total_unique_can_msg,
    total_runtime_of_data,
    avg_can_msg,
)

def main():
    csv_file = "data/gps_can_data.csv"
    print('Processing. Please wait...\n--------------------------')

    t1 = datetime.now()
    df = pd.read_csv(csv_file)
    print('Total GPS messages: ', total_gps_msg(df, 'gps_id'))
    print('Total CAN messages: ', total_can_msg(df, 'message_id'))
    print('Total unique CAN messages: ', total_unique_can_msg(df, 'dlc')) 
    print('Total runtime of data based on timestamp: ', total_runtime_of_data(df, 'ts'), 'seconds')
    print('Average CAN message per second of runtime and per GPS message: ', avg_can_msg(df, 'ts'))

    t2 = datetime.now()

    print('--------------------------')
    print(f'Finished in {(t2 - t1).total_seconds()} seconds')

if __name__ == '__main__':
    main()
