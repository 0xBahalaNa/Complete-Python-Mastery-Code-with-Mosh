"""
4. Functions, 07. xxargs

** before argument is a variation of *. 
Multiple keyword arguments returns key value pairs. 

This returns a dictionary. 
"""


def save_user(**user):
    print(user)


save_user(id=1, name="John", age=22)
"""
Output:
{'id': 1, 'name': 'John', 'age': 22}

"""
