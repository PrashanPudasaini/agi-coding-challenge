"""Entry point to the application. Run "python main.py"

A module with "main" that prints to stdout total gps message, total unique CAN messages, total CAN messages, total run time of data, 
average CAN message per second and per gps message, first timestamp with most most CAN messages, first timestamp
with least CAN messages

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 19th, 2022
"""
import opentracing
import lightstep
import pandas as pd #to read csv file
from datetime import datetime # to measure app performance
from core.helper import run_in_parallel
from core.utils import (
    total_gps_msg, # to compute total GPS message in a csv file
    total_can_msg, # to compute total CAN message in a csv file
    total_unique_can_msg, # to compute total unique CAN messages in a csv file
    total_runtime_of_data, #to compute total runtime of data based on timestamp
    avg_can_msg, #to compute average CAN message per second of run time and per GPS message
    first_ts_with_most_can_msg, # to compute timestamp that contains most CAN messages 
    first_ts_with_least_can_msg, # to compute timestamp that contains least CAN messages 
)

def main():
    
    csv_file = "data/gps_can_data.csv"
    print('Processing. Please wait...\n--------------------------\n')
    t1 = datetime.now()

    df = pd.read_csv(csv_file)
    print('1. Total GPS messages: ', total_gps_msg(df, 'gps_id'), '\n')
    print('2. Total CAN messages: ', total_can_msg(df, 'message_id'), '\n')
    print('3. Total unique CAN messages: ', total_unique_can_msg(df, 'message_id', 'dlc', 'payload'), '\n') 
    print('4. Total runtime of data based on timestamp: ', total_runtime_of_data(df, 'ts'), 'seconds \n')
    print('5. Average CAN message per second of runtime and per GPS message: ', avg_can_msg(df, 'ts'), '\n')
    print('6. First timestamp that contains the most CAN messages: ', first_ts_with_most_can_msg(df, 'ts'), '\n')
    print('7. First timestamp that contains the least CAN messages: ', first_ts_with_least_can_msg(df, 'ts'), '\n')

    t2 = datetime.now()
    print('--------------------------')
    print(f'Finished in {(t2 - t1).total_seconds()} seconds.')

if __name__ == '__main__':
    main()
