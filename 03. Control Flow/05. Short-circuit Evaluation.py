"""
3. Control Flow, 05. Short-circuit Evaluation

Short-circuit means that it starts from the first argument. 
If one of the arguments is not met, the function stops. 
One of the operands is False, evaluation stops. 
"""

high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")

"""
Output:

"""
