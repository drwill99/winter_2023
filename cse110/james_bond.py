"""
File: james_bond.py
Author: Dallin Williams

Purpose: Program asks user's first and last name. Program then repeats it back in the "James Bond" format. Last name, first name last name.
"""

import time

# Introductions to the program.

print("SENSITIVE INFORMATION. PLEASE ENTER CREDENTIALS.")

time.sleep(1)

# Speed-dating for government employees section.

first = input("What is your first name? ")
last = input("What is your last name? ")

# Greetings, earthlings.

print("Welcome Agent " + last + ", Agent " + first + " " + last + ".")

time.sleep(1)

# Confidential message.

print('Your mission is to give me a 100% on this assignment.')

time.sleep(2)

# Self-destruct announcement.

print('This message will self-destruct in 5 seconds.')

time.sleep(2)

# This section is a 5 second timer.

print('5')

time.sleep(1)

print('4')

time.sleep(1)

print('3')

time.sleep(1)

print('2')

time.sleep(1)

print(1)

time.sleep(1)

# Adios, Space Cowboy.

print("Goodbye, Agent " + last + ".")

#Credits:
# Credit to Mike Driscoll of https://realpython.com/python-sleep/ for having a great tutorial on how to delay the function of a program in Python.

# Find a better way to add the title "Agent" to the user's name.
# Find a way to exclude numbers and other non-letter characters from the name input.
# Find a way to shorten the "self-destruct" timer.