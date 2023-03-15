"""
5. Data Structures, 02. Accessing Items

Using square brackets (indexing and slicing) to modify elements a list.
[Start, stop, step].

Step is the interval amount. 
Negative step (-1) will reverse the list.
"""
letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])
print(letters[::3])

numbers = list(range(20))
print(numbers[::-2])
