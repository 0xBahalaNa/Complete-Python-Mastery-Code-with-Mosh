"""
3. Control Flow, 13. Infinte Loops

while loop that runs to infinity.
Add break statement to break out of loop.
Program might crash if it takes too much memory.
Always have a way to break out of a program.
"""
while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break

"""
"""
