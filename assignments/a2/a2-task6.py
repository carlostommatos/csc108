"""CSC108H1: Fall 2026 -- Assignment 2

Instructions (READ THIS FIRST!)
===============================

Make sure that the files a2_checker.py, a2_pyta.json, and checker_generic.py 
are in the same folder as this file (a2-task6.py).

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
#   Task 6   #
##############

TARGET = 5

my_list = ['rode', 'biked', 'ran', 'walked']

for i in range(len(my_list)):
    if len(my_list[i]) < TARGET:
        extra = '!' * (TARGET - len(my_list[i]))
        my_list[i] = my_list[i] + extra

print(my_list)