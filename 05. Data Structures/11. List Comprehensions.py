"""
5. Data Structures, 11. List Comprehensions

[expression for item in items]
List comprehension is cleaner. 
List comprehension is similar to the filter and map functions. 
"""

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]
# prices = list(map(lambda item: item[1], items))
prices = [item[1] for item in items]


# filtered = list(filter(lambda item: item[1] >= 10, items))
filtered = [item for item in items if item[1] >= 10]
