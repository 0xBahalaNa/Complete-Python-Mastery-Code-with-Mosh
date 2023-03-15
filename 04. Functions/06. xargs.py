"""
4. Functions, 06. xargs

Create a function that takes a variable number of arguments.

Use * and plural word to signify that its a collection of arguments. 

Tuple was created.
Tuples are immutable. 
Tuples are iterable. 
"""


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

"""
Output:
120

"""
