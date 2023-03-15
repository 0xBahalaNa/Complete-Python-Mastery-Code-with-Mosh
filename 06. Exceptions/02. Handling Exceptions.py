"""
6. Exceptions, 02. Handling Exceptions

Use try and except to handle exceptions. 

If user inputs the correct input, no exception will be thrown.
try block will not be executed.

Can add else statement as well.
"""
try:
    age = int(input("Age:"))
except ValueError as ex:
    print("You didn't enter a value age. ")
    print(ex)
    print(type(ex))
else:
    print("No exceptions were thrown.")
print("Execution continues. ")
"""
Output:
Age:a
You didn't enter a value age. 
invalid literal for int() with base 10: 'a'
<class 'ValueError'>
Execution continues. 
"""
