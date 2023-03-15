"""
5. Data Structures, 07. Sorting Lists


.sort method and sorted() methods.

Functions should be defined for sorting lists of tuples.

In the example below, the list of tuples is sorted by item price. 
"""
numbers = [3, 51, 2, 8, 6]
# numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))
print(numbers)
"""
Output:
[51, 8, 6, 3, 2]
[3, 51, 2, 8, 6]

"""

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item)
print(items)

"""
Output:
[('Product2', 9), ('Product1', 10), ('Product3', 12)]
"""
