"""
6. Exceptions, 05. The With Statement

with statement. 
Will always call .close() function. 

Magic methods utilize double underline (__method__).

Can open multiple resources with with statement. 
"""
try:
    with open(app.py) as file, open("another.txt" as target):
        print("File open. ")
        file.__enter__
    age = int(input("Age:"))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age. ")
else:
    print("No exceptions were thrown.")
