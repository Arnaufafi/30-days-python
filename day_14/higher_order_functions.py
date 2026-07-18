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

