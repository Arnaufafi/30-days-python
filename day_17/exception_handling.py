# Day 17 - 30DaysOfPython Challenge

# -----------------------------
# 1. Exception Handling
# -----------------------------
# Python uses try/except to handle errors gracefully.
#
# Basic structure:
# try:
#     # code that may fail
# except:
#     # code that runs if an error occurs
#
# You can catch specific exceptions:
# except TypeError:
# except ValueError:
# except ZeroDivisionError:
#
# Additional blocks:
# - else: runs if no exception occurs
# - finally: always runs
#
# Catching any exception:
# except Exception as e:
#     print(e)


# -----------------------------
# 2. Unpacking (* and **)
# -----------------------------
# * is used to unpack lists/tuples.
# ** is used to unpack dictionaries.
#
# Example (list unpacking):
# def sum_five(a, b, c, d, e):
#     return a + b + c + d + e
#
# lst = [1, 2, 3, 4, 5]
# sum_five(*lst)  # 15
#
# Unpacking with star operator:
# countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
# fin, sw, nor, *rest = countries
#
# Unpacking dictionaries:
# def person_info(name, country, city, age):
#     ...
#
# dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
# person_info(**dct)


# -----------------------------
# 3. Packing (*args and **kwargs)
# -----------------------------
# Packing allows functions to accept unlimited arguments.
#
# *args packs positional arguments into a tuple:
# def sum_all(*args):
#     return sum(args)
#
# **kwargs packs named arguments into a dictionary:
# def show_info(**kwargs):
#     for key in kwargs:
#         print(key, kwargs[key])


# -----------------------------
# 4. Spreading (like JavaScript)
# -----------------------------
# You can merge lists using *:
#
# lst_one = [1, 2, 3]
# lst_two = [4, 5, 6]
# combined = [0, *lst_one, *lst_two]
#
# country_one = ['Finland', 'Sweden', 'Norway']
# country_two = ['Denmark', 'Iceland']
# nordic = [*country_one, *country_two]


# -----------------------------
# 5. Enumerate
# -----------------------------
# enumerate() returns index + value when iterating.
#
# for index, item in enumerate([20, 30, 40]):
#     print(index, item)
#
# countries = ['Finland', 'Sweden', 'Norway']
# for index, country in enumerate(countries):
#     if country == 'Finland':
#         print(f'Found at index {index}')


# -----------------------------
# 6. Zip
# -----------------------------
# zip() allows parallel iteration over multiple lists.
#
# fruits = ['banana', 'orange', 'mango']
# vegetables = ['tomato', 'potato', 'cabbage']
#
# combined = []
# for f, v in zip(fruits, vegetables):
#     combined.append({'fruit': f, 'veg': v})
#
# print(combined)

## Exercices
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
# Unpack the first five countries and store them in a variable nordic_countries, 

nordic_countries = names[:5]
print(nordic_countries)

# Variant 
fin, swe, nor, den, ice, *rest = names
nordic_countries = [fin, swe, nor, den, ice]
print(nordic_countries)

# store Estonia and Russia in es, and ru respectively.
*others, es, ru = names
print(es)
print(ru)


