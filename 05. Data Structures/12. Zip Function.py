"""
5. Data Structures, 12. Zip Function

Combine multiple lists using zip function.
Can pass a string and apply it to the lists. 
Zip creates a list of tuples. 
"""

list1 = [1, 2, 3]
list2 = [10, 20, 30]

print(list(zip("abc", list1, list2)))

"""
Output:
[('a', 1, 10), ('b', 2, 20), ('c', 3, 30)]
"""
