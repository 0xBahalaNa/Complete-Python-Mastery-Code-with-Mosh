"""
7. Classes, 06. Magic Methods

Magic methods start and end with double underscore (__init__).
Magic methods are called automatically.

https://rszalski.github.io/magicmethods/
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
# point.__str__
print(point)
