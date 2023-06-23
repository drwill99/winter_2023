"""
File: loan_qualify.py
Author: Dallin Williams

Purpose: Determine whether or not to issue a loan based on user input.
"""

issue_loan = False

print()
print("To decide whether or not you qualify for a loan, \ngive each following variable a rating on a scale from 1-10:")
print()

loan_size = int(input("Loan size: "))
credit = int(input("Credit history: "))
income = int(input("Income: "))
down_payment = int(input("Down payment: "))

if loan_size >= 5:
    if credit >= 7 and income >= 7:
        issue_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            issue_loan = True
        else:
            issue_loan = False
    else:
        issue_loan = False
else:
    if credit < 4:
        issue_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            issue_loan = True
        elif income >= 4 and down_payment >= 4:
            issue_loan = True
        else:
            issue_loan = False

if issue_loan:
    print()
    print("Congratulations! You are qualified to owe us money!")
    print()
else:
    print()
    print("No loan for you! Stay poor, you bum!")
    print()