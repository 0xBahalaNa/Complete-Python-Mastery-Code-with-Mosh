"""
5. Data Structures, 05. Adding or Removing Items

Use dot (.) notation access methods in an object.
When a function is part of an object, its called a method. 

remove method removes the first iteration of object.
Loop is needed to remove all items.

del removes a range of items.
clear removes all objects in the list.

"""

letters = ["a", "b", "c"]
letters.append("d")
letters.insert(0, "-")
letters.pop()
letters.remove("b")
letters.clear()
del letters[0:3]
