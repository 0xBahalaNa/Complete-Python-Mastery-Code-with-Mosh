"""
2. Primitive Types, 06. String Methods

There are built in methods specific to strings.

Everything in Python is objects.

Use dot (.) notation. 

Returns new string doesn't affect original string. 

.strip() removes white space from string.

Many examples of methods. 

"""

course = "Python Programming"
print(course.upper())
print(course.lower())
print(course.title())
print(course.strip())
print(course.find("pro"))
print(course.replace("p", "j"))
print("Pro" in course)
print("swift" not in course)

"""
Output:
PYTHON PROGRAMMING
python programming
Python Programming
Python Programming
-1
Python Programming
True
True

"""
