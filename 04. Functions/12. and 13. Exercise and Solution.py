"""
4. Functions, 12. and 13. Exercise and Solution

FizzBuzz

Define a function called fizz_buzz. 
If the input is divisible by 3, return Fizz.
If the input is divisible by 5, return Buzz.
If the input is divisible by both 3 and 5, return FizzBuzz.
All other numbers return the input.
"""


def fizz_buzz(input):
    if input % 3 == 0 and input % 5 == 0:
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    else:
        return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(18))
print(fizz_buzz(19))


"""
Output:
Fizz
Buzz
FizzBuzz
Fizz
19 

"""
