"""
11. Popular Python Packages, 12. NumPy

NumPy is an important package used in scientific computations.
Useful for Data Science and Machine Learning.
Fast multi-dimensional arrays than pure Python.
"""

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])

# print(array)
# print(type(array))
# print(array.shape)

array = np.zeros((3, 4), dtype=int)
array = np.ones((3, 4), dtype=int)
array = np.full((3, 4), 5, dtype=int)
array = np.random((3, 4))
print(array)
print(array[0, 0])
print(array > 0.2)
print(array[array > 0.2])
print(np.sum(array))
print(np.floor(array))
print(np.ceil(array))
print(np.round(array))

first = np.array([1, 2, 3])
second = np.array([1, 2, 3])

print(first + second + 2)

dimensions_inch = np.array([1, 2, 3])
dimensions_cm = dimensions_inch * 2.54
print(dimensions_cm)
