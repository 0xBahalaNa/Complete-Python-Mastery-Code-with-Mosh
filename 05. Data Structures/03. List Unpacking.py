"""
5. Data Structures, 03. List Unpacking

Unpack a list into multiple variables.

Number of variables should equal the ammount of items in the list. 

Use asterisk (*) to pack other items into another list. 
"""
numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
first, *other, last = numbers

print(first, last)
print(other)
