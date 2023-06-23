"""
File: id_badge.py
Author: Dallin Williams

Purpose: Collect user information and display in an "ID badge" format.
"""

import time  # allows time functions to be utilized

print('Please enter the following information: ')
time.sleep(1)

# input section

first_name = input('First Name: ')
last_name = input('Last Name: ')
hair_color = input('Hair Color: ')
eye_color = input('Eye Color: ')
email_address = input('Email Address: ')
phone_number = input('Phone Number: ')
job_title = input('Job Title: ')
month_hired = input('Month Hired: ')
advanced_training = input('Completed Advanced Training? Yes or No: ')
id_number = input('ID Number: ')

# "generating simulation" section

print()
print('Please wait while your ID badge is generated.')
time.sleep(0.5)
print()
print('Generating...')
time.sleep(1)
print()

# personalized pick-up announcement

print(f"{first_name.title()} {last_name.title()}'s ID Badge: ")
time.sleep(1)
print()

# id badge section

print('----------------------------------------')
print(f'{last_name.upper()}, {first_name.title()}')
print(job_title.title())
print('ID # ' + id_number)
print()
print(email_address.lower())
print(phone_number)
print()
print(f"Hair: {hair_color.title():15} Eyes: {eye_color.title()}")
print(f"Month: {month_hired.title():14} Training: {advanced_training.title()}")
print('----------------------------------------')

# thank you, come again

time.sleep(1)
print()
print('Thank you, have a nice day!')
print ()

#CREDITS:
# Credit to the contributors of (https://www.pythoncheatsheet.org/cheatsheet/manipulating-strings#upper-lower-and-title) for helping me
# conceptualize case-formatting.

#IMPROVEMENTS:
# Add phone number and id number formatting. E.g., (123)-456-7890 for phone number, 12-345678 for id number
# Add a full border to the id badge, not just top and bottom.