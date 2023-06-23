"""
File: hr_system.py
Author: Dallin Williams

Purpose: Format and display contents of a file.
"""

print()

with open("hr_system.txt") as hr_file:
    for line in hr_file:
        line = line.strip()
        parts = line.split()

        name = parts[0]
        id = parts[1]
        title = parts[2]
        salary = float(parts[3])

        paycheck = salary / 24

        if title.lower() == "engineer":
            paycheck += 1000

        print(f"Name: {name.capitalize()} (ID: {id}), {title.capitalize()} - ${paycheck:.2f}")

print()