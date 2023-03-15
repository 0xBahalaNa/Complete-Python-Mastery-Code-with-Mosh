"""
7. Classes, 13. The Object Class

Object class. 
Base class of all classes of Python.
All classes inherit from the object class. 
"""


class Animal(object):
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


m = Mammal()
print(isinstance(m, object))
o = object()
print(issubclass(Mammal, Animal))
