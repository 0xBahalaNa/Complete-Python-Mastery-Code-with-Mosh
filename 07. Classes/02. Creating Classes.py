"""
7. Classes, 02. Creating Classes

Classes use Pascal naming convention. 
Variables and functions are all lowercase and separated by underscore.
First letter of every word is uppercase and no underscores. 

All methods should have a parameter called self. 
Inheritance. 
"""


class Point:
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, Point))

"""
Output:
<class '__main__.Point'>
True
"""
