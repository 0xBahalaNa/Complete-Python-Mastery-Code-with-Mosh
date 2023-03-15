"""
5. Data Structures, 04. Looping over Lists. 

Using loops over lists. 

enumerate function returns an enumerate object.
Returns a tuple. 
This example returns the index and the item in the index.
"""
letters = ["a", "b", "c"]
items = [0, "a"]
for index, letter in enumerate(letters):
    print(index, letter)

"""
Output: 
0 a
1 b
2 c

"""
