"""
7. Classes, 14. Method Overriding

Replace a method in the base class. 
Extending a method indentified in the base class. 
super() function calls __init__ in Animal class. 
"""


class Animal(object):
    def __init__(self):
        print("Animal Constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("walk")


m = Mammal()
print(m.age)
print(m.weight)
"""
Output:
Mammal Constructor
Animal Constructor
1
2
"""
