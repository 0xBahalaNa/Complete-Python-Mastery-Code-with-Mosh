"""
3. Control Flow, 09. For..Else

break statement breaks out of loops. 

for else statement
else statement will execute if for statement is not successful.
"""
successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
"""
Output:
Attempt
Successful
"""
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")
"""
Output:
Attempt
Attempt
Attempt
Attempted 3 times and failed
"""
