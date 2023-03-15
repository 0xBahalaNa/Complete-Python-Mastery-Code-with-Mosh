"""
6. Exceptions, 07. Cost of Raising Exceptions

Raising exceptions come at a cost.

Raising exceptions impact performance.
"""
from timeit import timeit

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
    """
code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age



xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
    """
print("first code", timeit(code1, number=10000))
print("second code", timeit(code2, number=10000))


"""
Output:
first code 0.004590000000462169
second code 0.0011329590015520807
"""
