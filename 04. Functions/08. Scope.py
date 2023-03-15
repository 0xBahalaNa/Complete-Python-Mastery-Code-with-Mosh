"""
4. Functions, 08. Scope

Scope refers to the region of the code where a variable is defined.
Anything within a function exists only within the function. 
Local variables to the function. Don't exist anywhere else.

Global variables are accessible through out the whole code. 

print function will reference the global variable not the function. 

If you use the global variable within a function, Python intepreter will reference the global. 

"""
message = "a"


def greet(name):
    # global message
    message = "b"


greet("Mosh")
print(message)
"""
Output:
a

"""
