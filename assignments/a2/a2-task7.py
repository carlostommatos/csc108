"""CSC108H1: Fall 2026 -- Assignment 2

Instructions (READ THIS FIRST!)
===============================

Make sure that the files a2_checker.py, a2_pyta.json, and checker_generic.py 
are in the same folder as this file (a2-task7.py).

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
#   Task 7   #
##############


values = [7, 5, 9]
items = values
nums = values[:]
# DO NOT CHANGE THE CODE ABOVE

removed = values.pop()
values.append(3)
nums.remove(5)

# DO NOT CHANGE THE CODE BELOW
print(values)
print(items)
print(nums)
print(removed)