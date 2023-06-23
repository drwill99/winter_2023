"""
File: meal_price_calculator.py
Author: Dallin Williams

Purpose: Calculate the total bill for a meal including tax and tip.
"""

import math
print()
print('Welcome to Los Pollos Hermanos!')
print()
app = float(input('How much were appetizers? $'))
drinks = float(input('How much were drinks? $'))
child = float(input("What's the price of a child's meal? $"))
adult = float(input("What's the price of an adult's meal? $"))
num_child = int(input('How many children are there? '))
num_adult = int(input('How many adults are there? '))
num_drinks = int(num_child + num_adult)
tax = float(input('What is the sales tax rate? '))
discount = int(input('What percentage is your discount? '))
tip = float(input('What percentage would you like to tip? '))
print('_________________________')
print('|')
subtotal = float(child * num_child + adult * num_adult + drinks * num_drinks + app) 
print(f'|Subtotal: ${subtotal:.2f}')
discount_subtotal = subtotal - (subtotal * (discount / 100))
print(f'|Discount: ${discount_subtotal:.2f}')
total_tip = float(subtotal * tip / 100)
print(f'|Tip: ${total_tip:.2f}')
sales_tax = float(subtotal + total_tip) * tax / 100
print(f'|Sales Tax: ${sales_tax:.2f}')
total = float(subtotal + sales_tax)
print(f'|Total: ${total:.2f}')
print('|')
pay = int(input('|Total Payment: $'))
change = float(pay - total)
print(f'|Change Due: ${change:.2f}')
print('|')
print('|Thank You, Come Again!')
print()

#IMPROVEMENTS:
# Make the output section look like a receipt.
# Add a discount formula.