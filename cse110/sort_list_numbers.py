"""
File: sort_list_numbers.py
Author: Dallin Williams

Purpose: Put numbers in lists and sort them. Find sum, average, smallest number, and largest number.
"""

print()
print("Enter a list of numbers.\nType 0 when finished.")

numbers = []
number = -1
sum = 0
largest = -1
smallest = 99999999999

while number != 0:
    print()
    number = int(input("Enter number: "))

    if number != 0:
        numbers.append(number)

for number in numbers:
    sum += number

print()
print(f"The sum is: {sum}")

count = len(numbers)
average = sum / count

print()
print(f"The average is: {average}")

for number in numbers:
    if number > largest:
        largest = number

print()
print(f"The largest number is: {largest}")

for number in numbers:
    if number > 0 and number < smallest:
        smallest = number

print()
print(f"The smallest positive number is: {smallest}")

sorted = sorted(numbers)

print()
print("The sorted list is: ")
for number in sorted:
    print(number)
 
print()