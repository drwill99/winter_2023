"""
File: area_of_shapes.py
Author: Dallin Williams

Purpose: Calculate the area of shapes from user input.
"""

import math

square_length = float(input('Length of one side of the square in cm: '))
square_area_cm = float(square_length ** 2)
square_area_m = float(square_area_cm / 10000)
print(f'Area of this square in cm\u00b2 = {square_area_cm} cm\u00b2')
print(f'Area of this square in m\u00b2 = {square_area_m} m\u00b2')
print()
rec_length = float(input('Length of rectangle in cm: '))
rec_height = float(input('Height of rectangle in cm: '))
rec_area_cm = float(rec_length * rec_height)
rec_area_m = float(rec_area_cm / 10000)
print(f'Area of this rectangle in cm\u00b2 = {rec_area_cm} cm\u00b2')
print(f'Area of this rectangle in m\u00b2 = {rec_area_m} m\u00b2')
print()
radius = float(input('Radius of the circle in cm: '))
circ_area_cm = float(math.pi * radius ** 2)
circ_area_m = float(circ_area_cm / 10000)
print(f'Area of this circle in cm\u00b2 = {circ_area_cm:.02f} cm\u00b2')
print(f'Area of this circle in m\u00b2 = {circ_area_m} m\u00b2')
print()

# stretch assignment (multiple area and volume calculations on one variable)

var = float(input('Enter a number: '))
print()
square_area_cm2 = float(var ** 2)
square_area_m2 = float(square_area_cm2 / 10000)
print(f'The area of a square with a length of {var} cm = {square_area_cm2:.02f} cm\u00b2')
print(f'Area of this square in m\u00b2 = {square_area_m2:.02f} m\u00b2')
print()
circ_area_cm2 = float(math.pi * var ** 2)
circ_area_m2 = float(circ_area_cm2 / 10000)
print(f'The area of a circle with a radius of {var} cm = {circ_area_cm2:.02f} cm\u00b2')
print(f'Area of this circle in m\u00b2 = {circ_area_m2:.02f} m\u00b2')
print()
cube_volume_cm = float(var ** 3)
cube_volume_m = float(cube_volume_cm / 10 ** 6)
print(f'The volume of a cube with a side of {var} cm = {cube_volume_cm:.02f} cm\u00b3')
print(f'Volume of this cube in m\u00b3 = {cube_volume_m:.02f} m\u00b3')
print()
sphere_volume_cm = float(4 / 3 * math.pi * var ** 3)
sphere_volume_m = float(sphere_volume_cm / 10 ** 6)
print(f'The volume of a sphere with the radius of {var} cm = {sphere_volume_cm:.02f} cm\u00b3')
print(f'Volume of this sphere in m\u00b3 = {sphere_volume_m:.02f} m\u00b3')
print()

#CREDITS:
# Credit to (https://www.inchcalculator.com/convert/cubic-centimeter-to-cubic-meter/) for explaining how to convert cm^3 to m^3

#IMPROVEMENTS:
# Find a neater, more user-friendly format to display outputs.