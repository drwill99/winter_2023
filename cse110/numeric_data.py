"""
File: numeric_data.py
Author: Dallin Williams

Purpose: Utilize numeric data from user input.
"""

age = int(input('Please enter your age: '))
print(f'Fun Fact: In a year, you will be: {age + 1}')

print()

eggs = int(input('How many cartons of eggs do you have? '))
print(f'Assuming your cartons hold 12 eggs, and are full, you have {eggs * 12} eggs.')

print ()

treat_type = input('What kind of treats are you sharing? ')
num_treats = int(input(f'How many {treat_type} do you have? '))
num_people = int(input('How many people are you sharing with? '))
treats_per = num_treats / num_people
print(f'Each person may have {treats_per} if split evenly.')
print()

#IMPROVEMENTS:
# Find a way to pluralize variable "treat_type" if not already plural.