# Day 13 - 30DaysOfPython Challenge

# [ expresión  for elemento in iterable  if condición ]

# Filter only negative and zero in the list using list comprehension 
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
x = lambda param : param <= 0
filtered_list = [n for n in numbers if x(n)]
print(numbers)
print(filtered_list)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_list = [number for row in list_of_lists for number in row]
print(list_of_lists)
print(flatten_list)

# Using list comprehension create the following list of tuples:
result = [(n, 1, n, n**2, n**3, n**4, n**5) for n in range(11)]
print(result)

# Flatten the following list to a new list: [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flatten_countries = [
                    [ country.upper(), country[:3].upper(), capital.upper() ]
                    for (country, capital) in (item[0] for item in countries)
                    ]
print(flatten_countries)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

dict_list = [{"country":country, "city":capital } for item in countries for (country,capital) in item]
print(dict_list)

# Change the following list of lists to a list of concatenated strings: ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_list = [f"{name} {surname}" for item in names for (name,surname) in item]
print(concatenated_list)