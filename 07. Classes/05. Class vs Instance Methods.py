"""
7. Classes, 05. Class vs Instance Methods

Class methods.
Reference to the class level.
Don't need an existing object.

Instance methods.
Used when using a specific object reference. 

cls method references the class.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()

"""
Output:
Point (0, 0)
"""
