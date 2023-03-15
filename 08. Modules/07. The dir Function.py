"""
8. Modules, 07. The dir Function

The dir function is built in.
List of attributes and methods defined in an object.
Used for debugging.
Shows an array of strings.
All the attributes of an object. 
"""
from ecommerce.shopping import sales

# print(dir(sales))
print(dir(sales.__name__))
print(dir(sales.__package__))
print(dir(sales.__file__))

"""
Output:
['__builtins__', '__cached__', '__doc__', '__file__', 
'__loader__', '__name__', '__package__', 
'__spec__', 'calc_shipping', 'calc_tax']
"""
