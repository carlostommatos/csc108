"""CSC108H1: Fall 2026 -- Assignment 2

Instructions (READ THIS FIRST!)
===============================

Make sure that the files a2_checker.py, a2_pyta.json, and checker_generic.py 
are in the same folder as this file (a2-task5.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students 
taking the CSC108H1 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2026 CSC108H1 Teaching Team
"""

##############
#   Task 5   #
##############

# Complete the function below according to its description by replacing each ?
# with the relevant code. Do not make any other changes to the code.

def count_doublings(target: int) -> int:
    """Return how many times we must double a number, starting from 1, to
    produce a value that is at least the value of target.

    >>> count_doublings(1)
    0
    >>> count_doublings(3)
    2
    >>> count_doublings(20)
    5
    """

    count = 0
    value = 1

    while value < target:
        count = count + 1
        value = value * 2

    return count
