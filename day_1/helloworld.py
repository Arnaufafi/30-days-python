# Day 1 - 30DaysOfPython Challenge

import math

print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# Checking data types
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

# Euclidean distance

x1, y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt((x2-x1)**2 + (y2 - y1)**2 )
print(f"Euclidean distance between {x1},{y1} and {x2},{y2} is {distance:.2f}")