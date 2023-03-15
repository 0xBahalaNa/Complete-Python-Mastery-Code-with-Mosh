"""
3. Control Flow, 14. Exercise

Write a program that displays all the even numbers between 1-10.
Expected Output:
2
4
6
8
We have 4 even numbers
"""
count = 0
for x in range(1, 10):
    if x % 2 == 0:
        print(x)
        count += 1
print(f"We have {count} even numbers")

"""
Output:
2
4
6
8
We have 4 even numbers
"""
