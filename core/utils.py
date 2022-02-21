"""Return from cvs file - total gps message, total unique CAN messages, total CAN messages, total run time of data, 
average CAN message per second and per gps message, first timestamp with most most CAN messages, first timestamp
with least CAN messages.

A module with "total_gps_message", "total_can_messages", " total_unique_can_messages", "total_run_time_of_data",
"avg_can_msg", "most_can_msg", "least_can_message" and main function that processes csv file read into a pandas
dataframe and prints the result to stdout.

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 18th, 2022
"""
import pandas as pd #to convert timestamp to python datetime
pd.set_option("display.max_rows", None, "display.max_columns", None)

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
    Total number of unique gps_id in the csv file
    """
    try:
        total_unique_gps_id = df[key].count()
    except KeyError:
        print(f'Cannot find key "{key}" in the dataframe.')
    else:
        return total_unique_gps_id

def total_can_msg(df, key):
    """Calculates the total number of message_id in the dataframe

    Parameters:
    __________
    df: pandas.DataFrame 
        The dataframe on which the oprations will be performed
    key: string
        The column name to perform operations on (key must be present in the dataframe)

    Returns:
    ________
    Total number of message_id in the csv file
    """
    try:
        total_msg_id = df[key].count() #count() to count only non-null values
    except KeyError:
        print(f'Cannot find key "{key}" in the dataframe.')
    else:
        return total_msg_id

def total_unique_can_msg(df, key):
    """Calculates the total number of unique CAN messages (message_id, dlc, payload) in the dataframe

    Parameters:
    __________
    df: pandas.DataFrame 
        The dataframe on which the oprations will be performed
    key: string
        The column name to perform operations on (key must be present in the dataframe)

    Returns:
    ________
    Total number of CAN messages in the csv file
    """
    try:
        total_unique_msg_id = len(df[key].value_counts())
        total_unique_dlc = len(df[key].value_counts())
        total_unique_payload = len(df[key].value_counts())
    except KeyError:
        print(f'Cannot find keys in the dataframe.')
    else:
        return total_unique_dlc

def total_runtime_of_data(df, key):
    """Calculates the total run time of data in the dataframe based on timestamp

    Parameters:
    __________
    df: pandas.DataFrame 
        The dataframe on which the oprations will be performed
    key: string
        The column name to perform operations on (key must be present in the dataframe)

    Returns:
    ________
    Total runtime of data (Last timestamp - First timestamp) in the dataframe
    """
    try:
        #Step 1: extract first timestamp in the dataframe
        first_ts = pd.to_datetime(df[key].iloc[0])
        #Step 2: extract last timestamp in the dataframe
        last_ts = pd.to_datetime(df[key].iloc[-1])
        #Step 3: Subtract first timestamp from last timestamp to get the total runtime
        total_runtime = (last_ts - first_ts).total_seconds() 
    except KeyError:
        print(f'Cannot find key "{key}" in the dataframe.')
    else:
        return total_runtime

def avg_can_msg(df, key):
    """Calculates the average CAN message per second of runtime and per GPS message

    Parameters:
    __________
    df: pandas.DataFrame 
        The dataframe on which the oprations will be performed
    key: string
        The column name to perform operations on (key must be present in the dataframe)

    Returns:
    ________
    Total runtime of data (Last timestamp - First timestamp) in the dataframe
    """
    try:
        total_can_msg = df[key].value_counts() - 1
        avg = total_can_msg.mean(axis = 0)
    except KeyError:
        print(f'Cannot find key "{key}" in the dataframe.')
    else:
        return avg

def first_ts_with_most_can_msg(df, key):
    """Finds the first timestamp that contains the most CAN messages

    Parameters:
    __________
    df: pandas.DataFrame 
        The dataframe on which the oprations will be performed
    key: string
        The column name to perform operations on (key must be present in the dataframe)

    Returns:
    ________
    First timestamp that contains the most CAN messsgaes
    """
    try:
        total_unique_ts = df['ts'].value_counts() - 1
        sorted_series = total_unique_ts.sort_index()

    except KeyError:
        print(f'Cannot find key "{key}" in the dataframe.')
    else:
        return sorted_series.idxmax()

def first_ts_with_least_can_msg(df, key):
    """Finds the first timestamp that contains the least CAN messages

    Parameters:
    __________
    df: pandas.DataFrame 
        The dataframe on which the oprations will be performed
    key: string
        The column name to perform operations on (key must be present in the dataframe)

    Returns:
    ________
    First timestamp that contains the least CAN messsgaes
    """
    try:
        total_unique_ts = df['ts'].value_counts() - 1
        sorted_series = total_unique_ts.sort_index()

    except KeyError:
        print(f'Cannot find key "{key}" in the dataframe.')
    else:
        return sorted_series.idxmin()
