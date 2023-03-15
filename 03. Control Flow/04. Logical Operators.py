"""
3. Control Flow, 04. Logical Operators

Three logical operators:
and, or, not

and both conditions must be True.

or one of the conditions must be True. 

not inverses the value of a Boolean.
if not True, then False
ie student = True, if not student:

"""
high_income = True
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Eligible")

"""
Output:
Eligible
"""

high_income = False
good_credit = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
"""
Output:
Not eligible
"""
high_income = False
good_credit = True

if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")
"""
Output:
Eligible
"""
high_income = False
good_credit = True
student = True

if not student:
    print("Eligible")
else:
    print("Not eligible")
"""
Output:
Not eligible
"""
high_income = False
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")

"""
Output:
Not eligible
"""
