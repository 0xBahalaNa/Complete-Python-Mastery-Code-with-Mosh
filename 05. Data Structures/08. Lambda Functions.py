"""
5. Data Structures, 08. Lambda Functions

Lambda function is a one line anonymous function that can be passed to other functions.
One time use. 

Syntax:
(key= lambda, parameters: expression)
"""
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]


items.sort(key=lambda item: item[1])
print(items)
