"""Return from cvs file - total gps message, total unique CAN messages, total CAN messages, total run time of data, 
average CAN message per second and per gps message, first timestamp with most most CAN messages, first timestamp
with least CAN messages.

A module with "total_gps_message", "total_can_messages", " total_unique_can_messages", "total_run_time_of_data",
"avg_can_msg", "most_can_msg", "least_can_message" and main function that processes csv file read into a pandas
dataframe and prints the result to stdout.

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 18th, 2022
"""

def total_gps_msg(df, key):
    """Calculates the total number of unique gps_id in the dataframe

    Parameters:
    __________
    df: pandas.DataFrame 
        The dataframe on which the oprations will be performed
    key: string
        The column name to perform operations on (key must be present in the dataframe)

    Returns:
    ________
    Total unique gps_id in the csv file
    """
    try:
        total_unique_gps_id = len(df[key].value_counts())
    except KeyError:
        print(f'Cannot find key "{key}" in the dataframe.')
    else:
        return total_unique_gps_id
