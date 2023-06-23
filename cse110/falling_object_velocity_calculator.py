"""
File: falling_object_velocity.py
Author: Dallin Williams

Purpose: Calculate the speed of a falling object using variables from user input.
"""

import math

print()
intro = "Welcome to the "
intro_center = intro.center(40)
print(intro_center)
print('Falling Object Velocity Calculator v1.0')
print()
print('Please enter the following information: ')
print()

m = float(input('Object mass in kg: '))
g = float(input('Acceleration due to gravity in m/s\u00b2: '))
# sun = 274.0, mercury = 3.7, venus = 8.87, earth = 9.81, earth's moon = 1.62, mars = 3.72
# jupiter = 24.79, saturn = 10.44, uranus = 8.87, neptune = 11.15, pluto = 0.62
t = float(input('Time elapsed in seconds: '))
p = float(input('Density of environmental fluid in kg/m\u00b3: '))
# earth's atmosphere = 1.293, water = 997.0
A = float(input('Cross-sectional area of object in m\u00b2: '))
C = float(input('Drag constant of object: '))
# sphere = 0.5, cube = 1.05, skydiver (horizontal) = 1.0, skydiver (diving) = 0.7,
# bicycle = 0.9, Ferrari Testarossa = 0.37, Toyota Camry = 0.28

c = (1 / 2) * p * A * C
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c) / m) * t))
v_terminal = math.sqrt(m * g / c)

print()
print(f'The inner value of c is {c:.3f}')
print()
print(f'The velocity after {t} seconds is {v:.3f} m/s')
print()
print(f'The terminal velocity is {v_terminal:.3f} m/s')
print()