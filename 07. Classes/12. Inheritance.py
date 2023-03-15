"""
7. Classes, 12. Inheritance

Classes might have one or more features or methods in common.
Methods can be in multiple classes and maybe be several lines.
Debugging can be hard for all the repeated methods.
Don't Repeat Yourself.

Inheritance.
Define the common methods of a class.
Parent/base class. Child/sub class.
Child/sub class inherits from parent/base class. 

Inherit the attributes of a base class. 

Below example gives an understanding of classes in relation to animals. 

"""


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
print(m.age)
"""
Output:
eat
1
"""
