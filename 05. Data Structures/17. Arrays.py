"""
5. Data Structures, 17. Arrays

Arrays are useful for large sequence of numbers if you encounter performance problems.

Import array module and has methods similar to lists. 

https://docs.python.org/3/library/array.html
"""
from array import array

numbers = array("i", [1, 2, 3])
numbers.append(4)
numbers.inset(1)
numbers.pop()
numbers[0]
