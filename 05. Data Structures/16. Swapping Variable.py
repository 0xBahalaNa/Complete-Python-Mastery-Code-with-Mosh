"""
5. Data Structures, 16. Swapping Variables

How to swap variables. 
Set a third variable.
Tuple unpacking.
Set variables on the left side to equal the values on the right side. 
"""
x = 10
y = 11

z = x
x = y
y = z
x, y = y, x
x, y = 11, 10
a, b = 1, 2

print("x", x)
print("y", y)
