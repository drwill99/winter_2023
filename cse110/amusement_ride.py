"""
File: amusement_ride.py
Author: Dallin Williams

Purpose: Check if amusement park customers can ride an attraction using user inputs and if-statements.
"""

print()
print("Welcome to Danger Dan's Waterpark and Nile Crocodile Rehabilitation Center!\n")
print("(Danger Dan's is not responsible for loss of personal items, limbs, or children. Thank you.)\n")

ride = False

age = int(input("Age of Rider #1 in years: "))
height = int(input("Height of Rider #1 in inches: "))

if age >= 12 and age < 18:
    golden = input("Does Rider have Golden Passport (yes/no): ")

second_rider = input("Second rider (yes/no): ")

if second_rider.lower() == "yes":
    age2 = int(input("Age of Rider #2 in years: "))
    height2 = int(input("Height of Rider #2 in inches: "))

    if age2 >= 12 and age2 < 18:
        golden2 = input("Does Rider have Golden Passport (yes/no): ")

    if height < 36 or height2 < 36:
        ride = False
    else:
        if age >= 18 or age2 >= 18 or golden.lower() == "yes" or golden2.lower() == "yes":
            ride = True
        else:
            if age >= 12 and height >= 52 and age2 >= 12 and height2 >= 52:
                ride = True
            elif (age >= 16 and age2 >= 14) or (age >= 14 and age2 >= 16):
                ride = True
            else:
                ride = False
else:
    if (age >= 18 or golden.lower() == "yes") and height >= 62:
        ride = True
    else:
        ride = False

if ride:
    print()
    print("Alright, get on and strap in. Y'all signed the waiver, right?\n")
else:
    print()
    print("Get the heck outta here, croc bait!\n")