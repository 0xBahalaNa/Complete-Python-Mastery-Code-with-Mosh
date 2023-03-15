"""
5. Data Structures, 15. Tuples

Tuples are read only. Cannot be modified.
Immutable.
Can define an empty tuple. 

Concatenate tuples. 

Pass tuple() to convert to a tuple.

Can use indexing in tuples. 

Tuples are used so items cannot be changed in code. 
"""
point = (1, 2) + (3, 4)
print(point)
x, y, z = point
if 10 in point:
    print("exists")
