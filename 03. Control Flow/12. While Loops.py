"""
3. Control Flow, 12. While Loops

while loops repeat something as long as something is True.
Evaluates a condition and repeats the task. 

.lower() will always terminate the command despite what the user input is. 
"""
number = 100
while number > 0:
    print(number)
    number //= 2

"""
Output:
100
50
25
12
6
3
1
"""

command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
