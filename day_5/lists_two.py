# Day 5 - 30DaysOfPython Challenge

from countries import countries

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
sorted_ages = ages
sorted_ages.sort()

ages_max = max(ages)
print(f"Max age: {ages_max}")
ages_max = sorted_ages[-1]
print(f"Max age: {ages_max}")

ages_min = min(ages)
print(f"Min age: {ages_min}")
ages_min = sorted_ages[0]
print(f"Min age: {ages_min}")

#Find the median age (one middle item or two middle items divided by two)
n = len(sorted_ages)
if n % 2 == 0:
    median_age = (sorted_ages[n//2 - 1] + sorted_ages[n//2]) / 2
else:
    median_age = sorted_ages[n//2]

print(f"Median age: {median_age}")

# Find the average age (sum of all items divided by their number )
total = 0
for age in sorted_ages:
    total = total + age

avarage_age = total/n
print(f"Avarage age: {avarage_age}")

# Find the range of the ages (max minus min)
age_range = ages_max - ages_min
print(f"Age range: {age_range}")

# Compare the value of (min - average) and (max - average), use abs() method
min_diff = abs(ages_min - avarage_age)
max_diff = abs(ages_max - avarage_age)

print(min_diff, max_diff)

#Find the middle country(ies) in the countries list
middle_country = countries[len(countries)//2]
print(f"\nMiddle country: {middle_country} \n")

n = len(countries)
half = n // 2 + (n % 2)
first_half = countries[:half]
second_half = countries[half:]

print(f"First half: {first_half} \n")
print(f"Second half: {second_half} \n")

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

first, second, third, *scandic = countries

print(f"First country: {first}")
print(f"Second country: {second}")
print(f"Third country: {third}")
print(f"Scandic countries: {scandic}")
