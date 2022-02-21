"""Run operations in parallel with multiprocessing.

A module with "run_in_parallel" that takes all functions and runs them in parallel with python multiprocessing. 
To be used for scaling purpose. Redundant for a small datasets.

Author: Prashan Pudasaini <prashan.pudasaini@outlook.com>

Created: February 18th, 2022
"""
from multiprocessing import Process #To run processes in parallel

def run_in_parallel(*fns):
    """Runs processes in parallel

    Parameters:
    __________
    fns: functions
    The functions to run in parallel
    """
    processes = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

