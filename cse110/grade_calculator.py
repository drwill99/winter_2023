"""
File: grade_calculator.py
Author: Dallin Williams

Purpose: Calculate letter grades from percentages from user input.
"""

print()
print("Welcome to the Strict Parent Simulator!\n")

grade = int(input("What is your grade percent (0-100)? "))

if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"

sign = ""

last_digit = grade % 10

if last_digit >= 7:
    sign = "+"
elif last_digit < 3:
    sign = "-"
else:
    sign = ""

if grade >= 93:
    sign = ""

if letter == "F":
    sign = ""

print()

print(f"Your letter grade is: {letter}{sign}")

print()

if grade == 100:
    print("Huh, you might be my kid after all... ")
elif grade >= 90:
    print("It's not 100%, but I guess you can continue living under my roof. ")
elif grade >= 80:
    print("I bet you think a B is pretty good, don't you? You'll never amount to anything if you settle for mediocrity!")
elif grade >= 70:
    print("Stay there, I'm going to get my belt with that big buckle... ")
elif grade >= 60:
    print("Get out of my house, and don't darken my doorway until you have better grades! ")
else:
    print("You're not even worth my time. Get out, and don't come back. ")

print()