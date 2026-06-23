# Day 2 - 30DaysOfPython Challenge

import math

# Exercises: Level 1
first_name = "Arnau"
last_name = "Fabregas"
full_name = f"{first_name} {last_name}"
country = "Spain"
city = "Tarragona"
age = 21
year = 2026
is_married, is_true, is_light_on = False, True, True

# Exercises: Level 2

variables = [first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on]

# Check the data type of all your variables using type() built-in function
for variable in variables:
    print(f"{variable} --> {type(variable)}")

# Compare the length of your first name and your last name
if len(first_name) > len(last_name):
    print(f"{first_name} is longer than {last_name} by {len(first_name) - len(last_name)} characters")
elif len(first_name) < len(last_name):
    print(f"{last_name} is longer than {first_name} by {len(last_name) - len(first_name)} characters")
else:
    print(f"Both words are equal and have {len(first_name)} characters")

# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two

# The radius of a circle is 30 meters.
radius = 30
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
area_of_circle = math.pi * radius**2

# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle = 2 * math.pi * radius

# Take radius as user input and calculate the area.
radius = float(input("Introduce the radius\n"))
area_of_circle = math.pi * radius**2
print(f"The area of the circle with radius: {radius}u is {area_of_circle:.3f}u")

# Use the built-in input function to get first name, last name, country and age from a user
first_name = input("Introduce your first name\n")
last_name = input("Introduce your last name\n")
country = input("Introduce your country\n")
age = int(input("Introduce your age\n"))

# Run help('keywords') to check Python reserved words
help("keywords")
