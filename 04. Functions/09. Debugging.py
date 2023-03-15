"""
4. Functions, 09. Debugging

Go to Debugging panel in VS Code. 
Utilize the breakpoint to start debugging.
Debugging goes through the code line by line. 
Step in line, step over line
"""


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))
"""
"""
