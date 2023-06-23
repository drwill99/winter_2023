"""
File: sync_two_lists.py
Author: Dallin Williams

Purpose: Have two lists affected by one input.
"""

print("\nEnter the names and balances of bank accounts (type: quit when done)")

names = []
balances = []

name = None
total = 0
change_account = "yes"

while name != "quit":
    name = input("What is the name of this account? ")

    if name != "quit":
        balance = float(input("What is the balance? "))

        names.append(name)
        balances.append(balance)

print("\nAccount Information: ")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]} - ${balances[i]:.2f}")

total += balances[i]
average = total / len(balances)

print(f"\nTotal: ${total:.2f}")
print(f"Average: ${average:.2f}\n")

highest_name = None
highest_balance = -1

for i in range(len(names)):
    name = names[i]
    balance = balances[i]

    if balance > highest_balance:
        highest_balance = balance
        highest_name = name

print(f"\nHighest balance: {highest_name} - ${highest_balance:.2f}")

while change_account == "yes":
    change_account = input("\nDo you want to update an account? ")

    if change_account == "yes":
        index = int(input("What account index do you want to update? "))
        new_amount = float(input("What is the new amount? "))

        balances[index - 1] = new_amount
    
    print("\nAccount Information:")
    for i in range(len(names)):
        print(f"{i + 1}. {names[i]} - ${balances[i]:.2f}\n")