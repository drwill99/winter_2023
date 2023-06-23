"""
File: windchill.py
Author: Dallin Williams

Purpose: Use def to convert float temperature to temperature with windchill.
"""

def calculates_wind_chill(t, v):
    return 35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * (v ** 0.16)
       
def converts_metric(temperature):
    return (temperature * 9 / 5) + 32

user_input_temp = float(input("What is the temperature?: "))
user_input_metric = (input("Fahrenheit or Celsius (F/C)?: "))

if user_input_metric.lower() == "c":
    user_input_temp = converts_metric(user_input_temp)

wind = 5
for i in range(12):
    windchill = calculates_wind_chill(user_input_temp, wind)
    print(f"At temperature {user_input_temp}F, and wind speed {wind} mph, the windchill is: {windchill:.2f}F")

    wind += 5