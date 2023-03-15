"""
5. Data Structures, 20. Dictionary Comprehensions

List comprehension is applicable to sets and dictionaries. 

Can't be used for tuples. 
"""
values = {x: x * 2 for x in range(5)}
print(values)

"""
Output:
{0: 0, 1: 2, 2: 4, 3: 6, 4: 8}
"""
