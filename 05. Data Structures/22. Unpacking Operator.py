"""
5. Data Structures, 22. Unpacking Operator

Print individual items from a list. 

Prefix with an asterisk (*). Double asterisks (**) for dictionaries.

Used on iterables. 
"""
numbers = [1, 2, 3]
print(*numbers)

values = [*range(5), *"Hello"]
print(values)

first = [1, 2]
second = [3]
values = [*first, "a", *second, *"Hello"]


first = {"x": 1}
second = {"x": 10, "y": 2}
combined = {**first, **second, "z": 1}
"""
Output:
1 2 3
[0, 1, 2, 3, 4, 'H', 'e', 'l', 'l', 'o']
"""
