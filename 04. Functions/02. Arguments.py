"""
4. Functions, 02. Variables

Passing inputs (arguments) in function. 

Difference between arguments and parameters.
Parameter is input you define for a function.
Argument is the actual value of a given parameter. 

Can pass different arguments when function is called.
All parameters are needed to call the function. 
"""


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Mosh", "Hamedani")
greet("John", "Smith")


"""
Output:
Hi Mosh Hamedani
Welcome aboard
Hi John Smith
Welcome aboard
"""
