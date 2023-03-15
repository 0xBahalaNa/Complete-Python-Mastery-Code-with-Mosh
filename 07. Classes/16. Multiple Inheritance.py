"""
7. Classes, 16. Multiple Inheritance

Classes that inherit from multiple other classes. 
Python will call the first method in the first class mentioned in a class with multiple inheritance. 
Multiple inheritance should be used properly. 
Things get complicated when classes have methods in common.
"""


class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()

# Good example of multiple inheritance below.


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass
