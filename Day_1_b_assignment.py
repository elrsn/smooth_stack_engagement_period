# Author: Elliott Larsen
# Date: 7/12/2022
# Description: Day 1-b assignment.

#--------------------------------------------------------------------------
# 1. Numbers: Example code to add two numbers 50+50 and 100-10 and print it.
#--------------------------------------------------------------------------
print(50 + 50) 
# output: 100

print(100 - 10)
# output: 90

#-------------------------------
# 2. 30+*6,6^6,6**6,6+6+6+6+6+6
#-------------------------------
print(30+*6)
# output:   
# File "/Users/name/Desktop/SmoothStack/Assignments/Day_1_b_assignment.py", line 12
#    print(30+*6)
#             ^
#SyntaxError: invalid syntax

print(6^6)
# output: 0

print(6**6)
# output: 46656

print(6+6+6+6+6+6)
# output: 36

#----------------------------------------------------------------------------------------------------------------------------
# 3. Print “Hello World” on the console output. Print output “Hello World : 10” Make sure capitalization and spacing matches.
#----------------------------------------------------------------------------------------------------------------------------
print("Hello World")
# output: Hello World

print("Hello World : 10")
# output: Hello World : 10

#------------------------------------------------
# 4. Below is a mathematical calculation exercise
#------------------------------------------------
def calculate_payment(principal, rate, length):
    """
    This function takes principal, interest rate, and length of the loan as parameters and returns the monthly payment amount.
    """
    monthly_rate = rate/100/12
    result = principal * (monthly_rate*(1 + monthly_rate) ** length) / ((1 + monthly_rate) ** length - 1)
    if result > int(result):
        return int(result) + 1
    return result

print(calculate_payment(800000, 6, 103))
# output: 9957
