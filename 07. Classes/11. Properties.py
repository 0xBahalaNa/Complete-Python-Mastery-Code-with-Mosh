"""
7. Classes, 11. Properties

Control over an attribute in a class. 
Property is an object that sits in front of an attribute and allows to get or set value of attribute. 
Create managed class attributes. 

Use decorators.
Use getters and setters.  
"""


class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = value


product = Product(-10)
print(product.price)
