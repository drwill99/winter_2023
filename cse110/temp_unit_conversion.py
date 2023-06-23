"""
File: temp_unit_conversion.py
Author: Dallin Williams

Purpose: To convert Fahrenheit to Celsius, Rankine, and Kelvin
"""

print()
temp_f = float(input('What is the temperature in Fahrenheit? '))
print()
temp_c = float(temp_f - 32) * 5 / 9
temp_k = float(temp_c + 273)
temp_r = float(temp_f + 460)
print(f'{temp_f:.1f}\u00b0 Fahrenheit is {temp_c:.1f}\u00b0 Celsius')
print()
print(f'{temp_f:.1f}\u00b0 Fahrenheit is {temp_k:.1f}\u00b0 Kelvin')
print()
print(f'{temp_f:.1f}\u00b0 Fahrenheit is {temp_r:.1f}\u00b0 Rankine')
print()