"""
9. Python Standard Library, 12. Generating Random Values

Random module.
Can be useful for generating a random password.
"""
import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print("".join(random.choices(string.ascii_letters + string.digits, k=4)))

print(string.ascii_letters)
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print(numbers)
