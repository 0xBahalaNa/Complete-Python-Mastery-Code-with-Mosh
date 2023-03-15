"""
6. Exceptions, 03. Handling Different Exceptions

Must specify the exceptions. 
Can have multiple except clauses in one except block. 
Separted by parenthesis.
"""
try:
    age = int(input("Age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age. ")
else:
    print("No exceptions were thrown.")

"""
Output:

Age:a
You didn't enter a valid age. 

Age:0
You didn't enter a valid age. 
"""
