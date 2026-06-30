# Day 5 - 30DaysOfPython Challenge

empty_list = []
list = ["Dog", "Cat", "Cow", "Bear", "Bee"]

#Length of my list
print(len(list))

#Get the first item, the middle item and the last item of the list

first_item = list[0]
middle_item = list[len(list) // 2]
last_item = list[-1]

print(first_item, middle_item, last_item)

mixed_data_types = ["Arnau", 21, 173, "Tarragona"]

it_companies = [ "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

first_it = it_companies[0]
middle_it = it_companies[len(it_companies) // 2]
last_it= it_companies[-1]

print(f"first: {first_it}, middle: {middle_it}, last: {last_it}")

# Print the list after modifying one of the companies
it_companies[0] = "Meta"
print(it_companies)

# Add an IT company to it_companies
it_companies.append("Intel")
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert((len(it_companies)//2), "Tesla")
print(it_companies)

# Change one of the it_companies names to uppercase
it_companies[-1] = it_companies[-1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined = "#; ".join(it_companies)
print(joined)

# Check if a certain company exists in the it_companies list.
print(f"Exists Apple ? {'Apple' in it_companies}")

# Sort and reverse
it_sorted = it_companies.sort()
print(it_sorted)
it_reverse = it_companies.reverse()
print(it_reverse)

print(it_companies)

# Slice out the first 3 companies from the list
first_slice = it_companies[:3]
print(first_slice)

#Slice out the last 3 companies from the list
last_slice = it_companies[-3:]
print(last_slice)

# Slice out the middle IT company or companies from the list
middle_it = len(it_companies) // 2
middle_slice = it_companies[middle_it]
print(middle_slice)

# Remove the first IT company from the list
it_companies.remove(it_companies[0])
print(it_companies)

# Remove the middle IT company or companies from the list
middle_it = len(it_companies) // 2
it_companies.remove(it_companies[middle_it])
print(it_companies)

# Remove all IT companies from the list
it_companies.remove(it_companies[-1])
print(it_companies)

# Destroy the IT companies list
it_companies.clear()
del it_companies

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
print(full_stack)

# Insert Python and SQL after Redux.
full_stack[5:5] = ["Python", "SQL"]
print(full_stack)