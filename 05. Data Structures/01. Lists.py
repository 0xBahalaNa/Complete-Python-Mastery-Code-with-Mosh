"""
5. Data Structures, 01. Lists

Lists use square brackets.
A sequence of objects.
Can have integers, floats, Booleans, and strings. 

A matrix is a two-dimensional list.

You can concatanate lists. 

Lists can have different types of objects.

list function to convert items into a list.

len function can see how many items are in a list. 
"""

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("Hello world")

len(chars)
