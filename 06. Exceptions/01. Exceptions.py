"""
6. Exceptions, 01. Exceptions

Display a proper error message to the user.

Errors are called Exceptions in Python.

Prevent program from crashing.
Errors and Exceptions
https://docs.python.org/3/tutorial/errors.html

Built-in Exceptions
https://docs.python.org/3/library/exceptions.html

"""
# numbers = [1, 2]
# print(numbers[3])

age = int(input("Age:"))
print(age)
"""
Output:
    print(numbers[3])
          ~~~~~~~^^^
IndexError: list index out of range

    age = int(input("Age:"))
          ^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'a'
"""
