"""
3. Control Flow, 02. Conditional Statements

if, while, else, elif statements.
Boolean values.
Terminate with a colon (:).
Indent after statement.
Evaluates if condition is True or False.
If condition is True, statement will execute whatever is in the block. 

elif is for multiple conditions after an if statement. 

else statement is if none of the previous conditions are met/are True. 

"""

temperature = 35
if temperature > 30:
    print("It's warm")
    print("Drink water")
print("Done")


"""
Output:
It's warm
Drink water
Done
"""

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
print("Done")

"""
Output:
Done
"""

temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 10:
    print("It's nice")
print("Done")

"""
Output:
It's nice
Done
"""
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

"""
Output:
It's cold
Done
"""
