"""
5. Data Structures, 21. Generator Expressions

Generator objects generate new values in each iteration.

Useful for large sets of data. Use the generator object function.

Use paranthesis around a comprehension function. 
"""
from sys import getsizeof
# values = (x * 2 for x in range(100000))
# print("gen:", getsizeof(values))
# print(values)
# for x in values:
#     print(x)
values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))

"""
Output:
<generator object <genexpr> at 0x7fe6c008f4a0>
0
2
4
6
8
10
12
14
16
18

list: 800984

"""
