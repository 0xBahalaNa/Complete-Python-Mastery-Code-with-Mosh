"""
3. Control Flow, 08. For Loops

Loops create repetition.
Terminate with colon(:).

Number start at 0. 

range(start, stop, step)

"""

for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")


"""
Output:
Attempt 1 .
Attempt 2 ..
Attempt 3 ...
"""

for number in range(1, 4):
    print("Attempt", number, number * ".")

"""
Output:
Attempt 1 .
Attempt 2 ..
Attempt 3 ...
"""

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
"""
Output:
Attempt 1 .
Attempt 3 ...
Attempt 5 .....
Attempt 7 .......
Attempt 9 .........
"""
