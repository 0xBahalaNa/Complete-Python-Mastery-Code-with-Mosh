"""
4. Functions, 05. Default Arguments

How to make parameters optional. 
Optional parameters should come after required parameters.
First parameter is needed and any other can be optional
"""


def increment(number, by=1):
    return number + by


print(increment(2, 5))

"""
Output:
7
"""
