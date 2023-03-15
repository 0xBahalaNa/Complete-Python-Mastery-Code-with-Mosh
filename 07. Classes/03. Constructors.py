"""
7. Classes, 03. Constructors

Constructor is needed for every new class created. 
Constructor initialize the class.
__init__ is a magic method. 

self references to the class.

"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(1, 2)
point.draw()
