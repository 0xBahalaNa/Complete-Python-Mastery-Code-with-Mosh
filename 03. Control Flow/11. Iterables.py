"""
3. Control Flow, 11. Iterables

range() function is iterable.
Strings are also iterable.
Lists are iterable
"""
print(type(5))
print(type(range(5)))

"""
Output:
<class 'int'>
<class 'range'>
"""
for x in "Python":
    print(x)
"""
Output:
P
y
t
h
o
n
"""

for x in [1, 2, 3, 4]:
    print(x)
"""
Output:
1
2
3
4
"""
