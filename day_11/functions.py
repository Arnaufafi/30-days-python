# Day 11 - 30DaysOfPython Challenge

import keyword
from math import sqrt
from countries_data import countries_data

## LEVEL 1

# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(a, b):
    return(a + b)

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(r, pi=3.14):
    return(pi * r * r)

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            return "All elemennts must be numbers"
    return total

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(c_degrees):
    return (c_degrees * 9/5) + 32

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(season):
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]

    if season in autumn:
        return("Autumn")
    elif season in winter:
        return("Winter")
    elif season in spring:
        return("Spring")
    elif season in summer:
        return("Summer")
    else:
        return(None)

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(a, b):
    if b == 0:
        return None
    return -a / b

# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a, b, c):
    main = b**2 - 4*a*c

    if a == 0:
        return "No solution"
    
    if main > 0:
        x1 = (-b + sqrt(main)) / (2*a)
        x2 = (-b - sqrt(main)) / (2*a)
        return(x1, x2)
    elif main == 0:
        x = -b / (2 * a)
        return(x, )
    else:
        real = -b / (2 * a)
        img = sqrt(-main) / (2 * a)
        return (complex(real, img), complex(real, -img))
    
# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(input_list):
    if type(input_list) != list:
        return None
    else:
        for element in input_list:
            print(element)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(input_list):
    if type(input_list) != list:
        return None
    
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    
    return reversed_list

# Variant
def reverse_list_var(input_list):
    if type(input_list) != list:
        return None
    else:
        return input_list[::-1]
 
print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list_var([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
print(reverse_list_var(["A", "B", "C"])) 
# ["C", "B", "A"]

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(input_list):
    if type(input_list) != list:
        return None
    else:
        capitalized_list = []
        for item in input_list:
            capitalized = str(item).capitalize()
            capitalized_list.append(capitalized)
    
    return capitalized_list

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(input_list, new_item):
    if type(input_list) != list:
        return None
    
    return_list = input_list.copy()
    return_list.append(new_item)
    return return_list

    
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk'];
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
numbers = [2, 3, 7, 9];
print(add_item(numbers, 5))      # [2, 3, 7, 9, 5]

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(input_list, r_item):
    if type(input_list) != list:
        return None
    
    return_list = input_list.copy()
    return_list.remove(r_item)
    return return_list

food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(range):
    i = 0
    sum = 0
    
    while i <= range:
        sum += i
        i+=1
    return sum

print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(range):
    i = 0
    sum = 0
    
    while i <= range:
        if i % 2 != 0:
            sum += i
        i+=1
    return sum

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(range):
    i = 0
    sum = 0
    
    while i <= range:
        if i % 2 == 0:
            sum += i
        i+=1
    return sum   

## LEVEL 2

# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(number):

    evens, odds = 0, 0

    for value in range(number + 1):
        if value % 2 == 0:
            evens += 1
        else:
            odds += 1
    
    return(evens, odds)
    
evens, odds = evens_and_odds(100)
print(f"The number of odds are {odds}\nThe number of evens are {evens}")

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):

    factorial = 1

    for value in range(1, number + 1):
        factorial *= value
    
    return factorial

print(f"The factorial of 5 is {factorial(5)}")

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    return not param

# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, 
# calculate_variance, calculate_std (standard deviation

def calculate_mean(input_list):
    total = sum(input_list)
    return total / len(input_list)


def calculate_median(input_list):
    input_list.sort()
    n = len(input_list)
    mid = n // 2

    if n % 2 == 0:
        return (input_list[mid - 1] + input_list[mid]) / 2
    else:
        return (input_list[mid])

def calculate_mode(input_list):
    input_list.sort()

    mode_number, actual_number, acumm , max = input_list[0], input_list[0], 0, 0

    for number in input_list:
        if number ==  actual_number:
            acumm += 1
            if acumm > max:
                max = acumm
                mode_number = number
        else:
            actual_number = number
            acumm = 1

    return mode_number

def calculate_range(input_list):
    input_list.sort()
    return(input_list[0], input_list[-1])

def calculate_variance(input_list):
    mean = calculate_mean(input_list)
    squared_diffs = [(x-mean) ** 2 for x in input_list]
    variance = sum(squared_diffs) / len(input_list)
    return variance

def calculate_std(input_list):
    return calculate_variance(input_list) ** 0.5

# Write a function called greet which takes a default argument, name. 
# If no argument is supplied it should print "Hello, Guest!", otherwise it should greet the person by name.

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Pablo")

# Create a function called show_args to take an arbitrary number of named arguments and print their names and values.

def show_args(**args):
    for name, value in args.items():
        print(f"Name: {name}, Value: {value}")

show_args(name="Alice", age=30, city="New York")
show_args(name="Bob", pet="Fluffy, the bunny")

## LEVEL 3

# Write a function called is_prime, which checks if a number is prime.

def is_prime(number):
    if number <= 1:
        return False
    
    if number % 2 == 0 and number != 2:
        return False
    
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
        
    return True

tests = [2, 7, 10, 97]
for n in tests:
    print(f"Number {n:<3} is {'Prime' if is_prime(n) else 'Not prime'}")

# Write a functions which checks if all items are unique in the list.
def unique_items(input_list):
    new_set = set(input_list)
    return (len(input_list) == len(new_set))

# Write a function which checks if all the items of the list are of the same data type.
def same_type(input_list):
    return len({type(x) for x in input_list}) == 1

# Write a function which check if provided variable is a valid python variable
def valid_variable(variable):
    return variable.isidentifier() and not keyword.iskeyword(variable)

# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

def most_spoken_languages(countries_data):
    spoken_count = {}

    for country in countries_data:
        population = country["population"]
        for language in country["languages"]:
            spoken_count[language] = spoken_count.get(language, 0) + population

    top20 = sorted(spoken_count.items(), key = lambda x: x[1], reverse=True)[:20]

    return top20

print(most_spoken_languages(countries_data))

def most_populated_countries(countries_data):
    
    top20 = sorted(countries_data, key= lambda x: x["population"], reverse=True)[:20]

    return top20