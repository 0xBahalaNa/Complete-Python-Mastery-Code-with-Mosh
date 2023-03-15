"""
5. Data Structures, 18. Sets

Sets a collection of items with no duplicates.

Use pipe operator (|) to add two sets together. 

Intersection of two sets (&). New set that contain items in both sets.

Difference between two sets (-).

Symmetric difference (^). Returns items in first or second sets, not both.

Sets don't allow for indexing. 
"""
numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 4}
print(first | second)
print(first & second)
print(first - second)
print(first ^ second)


"""
Output:
{1, 2, 3, 4}
{1, 4}
{2, 3}
{2, 3}
"""
