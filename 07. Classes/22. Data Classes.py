"""
7. Classes, 22. Data Classes

Classes that don't have any methods, just data.
Namedtuple instance.
Best used for classes that only have data.
Don't need to define a method to compare objects.
"""
from collections import namedtuple


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p1 = Point(x=10, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
