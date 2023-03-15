"""
5. Data Structures, 10. Filter Function

Filter function uses a lambda function. 

filter(function, iterable)
"""
items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

filtered = list(filter(lambda item: item[1] >= 10, items))
print(filtered)

"""
Output:
[('Product1', 10), ('Product3', 12)]
"""
