"""CSC108H1: Fall 2026 -- Assignment 2

Instructions (READ THIS FIRST!)
===============================

Make sure that the files a2_checker.py, a2_pyta.json, and checker_generic.py 
are in the same folder as this file (a2.py).

Copyright and Usage Information
===============================

This code is provided solely for the personal and private use of students 
taking the CSC108H1 course at the University of Toronto. Copying for purposes 
other than this use is expressly prohibited. All forms of distribution of 
this code, whether as given or with any changes, are expressly prohibited.

All of the files in this directory and all subdirectories are:
Copyright (c) 2026 CSC108H1 Teaching Team
"""

# Constants

# For Task 1
VOWELS = 'aeiouAEIOU'

##############
#   Task 1   #
##############

# Follow the function design recipe to write the count_vowels
# function according to its description.

def count_vowels(word: str) -> int:
    """Return the number of vowels in word.

    >>> count_vowels("hello")
    2
    >>> count_vowels("banana")
    3
    """
    count = 0

    for ch in word:
        if ch in VOWELS:
            count += 1
    return count

##############
#   Task 2   #
##############

# Follow the function design recipe to write the sum_evens
# function according to its description.

# Restriction: you must not use an if statement.

def sum_evens(start: int, stop:  int) -> int:
    """ Return the sum (total) of all even numbers
    from start to stop (inclusive).

    >>> sum_evens(0, 10)
    30
    >>> sum_evens(4, 4)
    4
    """

    total = 0

    for i in range(start, stop + 1, 2):
        total += i
    return total

##############
#   Task 3   #
##############

# Follow the function design recipe to write the find_cheapest
# function according to its description.

# Restriction: you must not use the built-in functions min, max, or sorted, 
# or the list method sort.

def find_cheapest(prices: list[float]) -> float:
    """ Return the lowest price in prices.

    >>> find_cheapest([20.00, 99.99, 5.49])
    5.49

    >>> find_cheapest([500.00, 15.00, 75.00])
    15.0
    """

    cheapest = prices[0]

    for p in prices:
        if p < cheapest:
            cheapest = p
    return cheapest

##############
#   Task 4   #
##############


# Although the given docstring example passes, the function below does not work
# according to its docstring. 
# a) Add a second example that meets the docstring description, but fails for
#    this implementation.
# b) Next, fix the code so that the examples both pass and the function works
#    according to its description.

def make_lowercase(words: list[str]) -> None:
    """Convert the strings in words to lowercase.

    >>> items = ['hey!', 'how', 'are', 'you?']
    >>> make_lowercase(items)
    >>> items
    ['hey!', 'how', 'are', 'you?']

    >>> items = ['HEY!', 'HOW', 'ARE', 'YOU?']
    >>> make_lowercase(items)
    >>> items
    ['hey!', 'how', 'are', 'you?']
    """

    for item in range(len(words)):
        words[item] = words[item].lower()
