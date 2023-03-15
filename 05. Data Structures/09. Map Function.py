"""
5. Data Structures, 09. Map Function

Map function.
Transform a list.
Takes a lambda function and applies to every item of an iterable. 
"""

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

x = list(map(lambda item: item[1], items))
print(x)
