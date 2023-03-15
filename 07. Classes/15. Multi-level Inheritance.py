"""
7. Classes, 15. Multi-level Inheritance

Too much inheritance can introduce some issues. 
Limit inheritance to one or two classes. 
"""


class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass
