"""
6. Exceptions, 04. Cleaning Up

External resources such as files, databases, etc.
Open a file, close it when done. 

Finally clause.
Close files, database connections etc.
Will always execute. 
"""
try:
    file = open(app.py)
    age = int(input("Age:"))
    xfactor = 10 / age
    file.close()
except (ValueError, ZeroDivisionError):
    print("You didn't enter a valid age. ")
else:
    print("No exceptions were thrown.")
finally:
    file.close()
