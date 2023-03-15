"""
7. Classes, 07. Comparing Objects

Compares two different things in memory. 

https://rszalski.github.io/magicmethods/

Define all the different magic methods necessary for your class. 
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y


point = Point(10, 20)
other = Point(1, 2)
print(point < other)


"""
Output:
False
"""
