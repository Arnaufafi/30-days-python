# Day 3 - 30DaysOfPython Challenge

import math

age = 21
height = 1.70
z = 3 + 5j

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
triangle_base = float(input("Introduce triangle base\n"))
triangle_height = float(input("Introduce triangle height\n"))
triangle_area = (triangle_base * triangle_height)/2
print(f"The area of the triangle is {triangle_area}u\n")

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
tri_side_a = float(input("Introduce side A\n"))
tri_side_b = float(input("Introduce side B\n"))
tri_side_c = float(input("Introduce side C\n"))
triangle_perimeter = tri_side_a + tri_side_b + tri_side_c
print(f"The perimeter of the triangle is {triangle_perimeter}u\n")

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
rect_len = float(input("Introduce rectangle length\n"))
rect_width = float(input("Introduce rectangle width\n"))
rect_area = rect_len * rect_width
rect_peri = rect_width*2 + rect_len*2
print(f"The area of the rectangle is {rect_area}u and the perimeter of the rectangle is {rect_peri}u\n")

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Introduce the radius\n"))
pi = 3.14
circle_area = pi * radius**2
circle_circum = 2 * pi * radius
print(f"The area of the circle is {circle_area}u and the circumference is {circle_circum}u\n")

# Calculate the slope, x-intercept and y-intercept of y = 2x -2
m1 = 2
b = -2
x_intercept = -b / m1
print(f"Slope(m): {m1}\nY-intercept (b): {b}\nX-intercept: {x_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, x2, y1, y2 = 2, 6, 2, 10
m2 = ((y2-y1)/(x2-x1))
euclidean_dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)

#Compare the slopes in tasks 8 and 9.
diff_slopes = abs(m2-m1)

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
def equation(x):
    return x**2 + 6*x + 9

for x in range (-10, 11):
    print(f"x:{x} --> res:{equation(x)}\n")

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
falsy = len("python") > len("dragon")

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "on" in "dragon")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")

# There is no 'on' in both dragon and python
print("on" not in "dragon" and "on" not in "python" )

# Find the length of the text python and convert the value to float and convert it to string
word_len = str(len("python"))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 2
if (number % 2 == 0 ): print("even")
else: print("odd")

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(f"Is the floor division of 7 by 3 is equal to the int converted value of 2.7: {7//3 == int(2.7)}")

# Check if type of '10' is equal to type of 10
print(f"Is type of '10' is equal to type of 10: {type(10) == type('10')}")

# Check if int('9.8') is equal to 10
print(f"Is int('9.8') is equal to 10: {int(float('9.8')) == 10}")

# Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
enter_hours = float(input("Introduce your enter hours\n"))
rate_hour = float(input("Introduce your rate per hour\n"))
print(f"Enter hours: {enter_hours}\n Rate per hour: {rate_hour}\n Your weekly earning is: {enter_hours * rate_hour}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years_lived = float(input("Introduce your age\n"))
print(f"You have lived for {years_lived*31536000} seconds.")

# Write a Python script that displays the following table
for i in range(1, 6):
    print(i, 1, i, i**2, i**3)
