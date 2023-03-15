"""
5. Data Structures, 19. Dictionaries

A dictionary is a collection of key value pair. 
Mappings. 

Can only use immutable types for the keys. Strings and numbers.
Values can be of any type.
dict function to create a dictionary.
Utilize keyword arguments to create a dictionary using dict() function.

To index, use the key. 
"""
point = {"x": 1, "y": 2}
point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
print(point.get("a", 0))
del point["x"]
print(point)
for x in point.items():
    print(x)
"""
Output:
0
{'y': 2, 'z': 20}
('y', 2)
('z', 20)
"""
