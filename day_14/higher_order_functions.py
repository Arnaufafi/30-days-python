# Day 14 - 30DaysOfPython Challenge

# Explain the difference between map, filter, and reduce.

# -----------------------------
# MAP → transform each element
# -----------------------------
# Applies a function to every element in an iterable.
# Returns a new iterable with the transformed values.
# Example: square each number.
# result = map(lambda x: x**2, [1, 2, 3])
# -> [1, 4, 9]

# -----------------------------
# FILTER → keep only elements that match a condition
# -----------------------------
# Applies a function that returns True/False.
# Keeps only the elements for which the function returns True.
# Example: keep only even numbers.
# result = filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
# -> [2, 4]

# -----------------------------
# REDUCE → combine all elements into a single value
# -----------------------------
# Applies a function that accumulates values step by step.
# Returns ONE final value instead of an iterable.
# Note: reduce is in functools, so you must import it.
# Example: sum all numbers.
# from functools import reduce
# result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
# -> 10

# Explain the difference between higher order function, closure and decorator

# -----------------------------------------
# HIGHER ORDER FUNCTION
# -----------------------------------------
# A higher-order function is any function that:
#   1. Takes another function as an argument, OR
#   2. Returns a function.
#
# This allows functions to be treated as data.
#
# Example:
# def apply_function(f, x):
#     return f(x)
# apply_function is a higher-order function because it receives a function.


# -----------------------------------------
# CLOSURE
# -----------------------------------------
# A closure occurs when:
#   - A nested (inner) function captures variables from the outer function,
#   - And the inner function remembers those variables even after the outer
#     function has finished executing.
#
# Closures allow functions to "remember" the environment where they were created.
#
# Example:
# def make_adder(n):
#     def add(x):
#         return x + n   # 'n' is remembered → closure
#     return add
# add5 = make_adder(5)
# add5(10)  # returns 15


# -----------------------------------------
# DECORATOR
# -----------------------------------------
# A decorator is a special type of higher-order function that:
#   - Wraps another function,
#   - Adds extra behavior,
#   - Without modifying the original function's code.
#
# Decorators use the @ syntax.
#
# Example:
# def uppercase_decorator(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
#
# @uppercase_decorator
# def greet():
#     return "hello"
#


# Define a call function before map, filter or reduce, see examples.

from functools import reduce


def square(x):
    return x*x

result = map(square, [1, 2, 3])
print(list(result))

def is_even(x):
    return x % 2 == 0

result = filter(is_even, [1,2,3,4])
print(list(result))

def add(x, y):
    return x + y

result = reduce(add, [1, 2, 3, 4])
print(result)

# Use map to create a new list by changing each country to uppercase in the countries list
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']

result = map(lambda country: country.upper(), countries)
print(list(result))

# Use map to create a new list by changing each number to its square in the numbers list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = map(square, numbers)
print(list(result))

# Use map to change each name to uppercase in the names list
names = names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

result = map(lambda name : name.upper(), names)

# Use filter to filter out countries containing 'land'.
result = filter(lambda country: "land" in country, countries )
print(list(result))

# Use filter to filter out countries having exactly six characters.
result = filter(lambda country: len(country) == 6, countries)
print(list(result))

# Use filter to filter out countries containing six letters and more in the country list.
result = filter(lambda country: len(country) >= 6, countries)
print(list(result))

# Use filter to filter out countries starting with an 'E
result = filter(lambda country: country[0] == "E", countries)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))
result = map(lambda country: country.upper(),filter(lambda country: len(country) == 6, countries))
print(list(result))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_list(input_list):
    return list(filter(lambda item: isinstance(item, str), input_list))

# Use reduce to sum all the numbers in the numbers list.
result = reduce(lambda x, y: x+y, numbers)
print(result)

