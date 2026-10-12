"""A simple checker for types of functions in a2.py and a2-task5.py.

Checks that your functions exist, return the right type, and that your memory
model files run. It does NOT check correctness.

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students
taking the CSC108H1 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2026 CSC108H1 Teaching Team
"""

import unittest

import checker_generic

FILENAME = 'a2.py'
TASK5_FILENAME = 'a2-task5.py'
PYTA_CONFIG = 'a2_pyta.json'
TARGET_LEN = 79
SEP = '='


class TestChecker(unittest.TestCase):
    """Sanity checker for assignment functions."""

    # Task 1
    def test_task1_count_vowels(self) -> None:
        """Function count_vowels."""

        func = checker_generic.get_function(FILENAME, 'count_vowels', 'Task 1')
        checker_generic.check_type(func, ['Happy day!'], int)

    # Task 2
    def test_task2_sum_evens(self) -> None:
        """Function sum_evens."""

        func = checker_generic.get_function(FILENAME, 'sum_evens', 'Task 2')
        checker_generic.check_type(func, [4, 6], int)

    # Task 3
    def test_task3_find_cheapest(self) -> None:
        """Function find_cheapest."""

        func = checker_generic.get_function(
            FILENAME, 'find_cheapest', 'Task 3')
        checker_generic.check_type(func, [[9.99, 5.75, 2.22]], float)

    # Task 4
    def test_task4_make_lowercase(self) -> None:
        """Function make_lowercase."""

        func = checker_generic.get_function(
            FILENAME, 'make_lowercase', 'Task 4')
        checker_generic.check_type(func, [['Hey!', 'How']], type(None))

    def test_task4_docstring_examples(self) -> None:
        """Docstring examples for make_lowercase."""

        func = checker_generic.get_function(
            FILENAME, 'make_lowercase', 'Task 4')
        checker_generic.check_docstring_calls(func, 2, 'Task 4')

    # Task 5
    def test_task5_count_doublings(self) -> None:
        """Function count_doublings in a2-task5.py."""

        func = checker_generic.get_function_from_file(
            TASK5_FILENAME, 'count_doublings', 'Task 5')
        checker_generic.check_type(func, [20], int)

    # Task 6
    def test_task6(self) -> None:
        """Memory model file a2-task6.py."""

        checker_generic.check_memory_model_file('Task 6')

    # Task 7
    def test_task7(self) -> None:
        """Memory model file a2-task7.py."""

        checker_generic.check_memory_model_file('Task 7')


print(''.center(TARGET_LEN, SEP))
print(' Start: checking coding style with PythonTA '.center(TARGET_LEN, SEP))
checker_generic.run_pyta(FILENAME, PYTA_CONFIG)
checker_generic.run_pyta(TASK5_FILENAME, PYTA_CONFIG)
print(' End checking coding style with PythonTA '.center(TARGET_LEN, SEP))

print(' Start: checking type contracts, docstrings, memory models '
      .center(TARGET_LEN, SEP))
unittest.main(exit=False, buffer=True)
print(' End checking type contracts, docstrings, memory models '
      .center(TARGET_LEN, SEP))

print('\nScroll up to see ALL RESULTS:')
print('  - checking coding style with Python TA')
print('  - checking type contracts')
print('  - checking docstrings')
print('  - checking memory models\n')
