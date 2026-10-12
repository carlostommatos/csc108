"""Week 5 Perform - Part 2"""
# file name: w05_markus.py
#
# Complete the following steps:
#  (1) Complete the following function according to its docstring.
#  (2) Save your file after you make changes, and then run the file by
#      clicking on the green Run button in Wing101. This will let you call your
#      modified function in the Python shell. An asterisk * on the Wing101
#      w05_markus.py tab indicates that modifications have NOT been saved.
#  (3) Test your function in the Wing101 shell by evaluating the examples from
#      the docstring and confirming that the correct result is displayed.
#  (4) Test your function using different function arguments.
#  (5) When you are convinced that your function is correct, submit your
#      modified file to MarkUs. You can find instructions on submitting a file
#      to MarkUs in Week *2* Perform -> Accessing Part 2 of the
#      Week 2 Perform (For Credit) on PCRS.
#  (6) Verify you have submitted the right file to MarkUs by downloading it
#      and checking that the downloaded file is the one you meant to submit.
#  (7) We have also provided a checker test for you to run on MarkUs. Click on
#      the Automated Testing tab and then Run tests to make sure your code
#      passes our simple test case. Go back to step (1) if errors were reported
#      and modify your work.  You may need to click on some arrows to see all
#      of the error report. Note that we will run additional tests when we mark
#      your submission.


def first_odd(items: list[int]) -> int:
    """Return the first odd number from items. Return 0 if items does not
    contain any odd numbers.

    >>> first_odd([6, 8, 3, 2])
    3
    >>> first_odd([2, 4])
    0
    """
    for i in items:
        if i % 2 == 1:
            return i
    return 0

