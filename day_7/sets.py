# Day 7 - 30DaysOfPython Challenge

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Exercises: Level 1
print(f"The length of the set it is: {len(it_companies)}\n")

# Add 'Twitter' to it_companies
print(it_companies)
it_companies.add("Twitter")
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(["Google", "Meta", "Anthropic", "OpenAI"]) # Google is a duplicate and will not be added to the set.
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies.remove("Google")
print(f"Remove Google\n{it_companies}")

# What is the difference between remove and discard
it_companies.discard("Meta")
it_companies.discard("Meta") # Error is ignored, if element does not exists nothing happen
print(f"Discard Meta\n{it_companies}")

# Exercises: Level 2

# Join A and B

joined_AB = A.union(B)
print(joined_AB)

# Find A intersection B

intersected_AB = A.intersection(B)
print(intersected_AB)

# Is A subset of B
print(f"Is A subset of B ? {A.issubset(B)}")

# Are A and B disjoint sets
print(f"Are A and B disjoint sets ? {A.isdisjoint(B)}")

# Join A with B and B with A
print(f"Join A with B: {A.union(B)}\nJoin B with A: {B.union(A)}")

# What is the symmetric difference between A and B
print(f"The symetric difference between A and B is: {A.symmetric_difference(B)}\n")

# Delete the sets completely
del A
del B
del it_companies

# Exercises: Level 3

# Convert the ages to a set and compare the length of the list and the set
ages_set = set(age)
print(f"Length list = {len(age)}\nLength set = {len(ages_set)}")

# Explain the difference between the following data types: string, list, tuple and set
string_info = "String: ordered, immutable, allows duplicates, indexable."
list_info = "List: ordered, mutable, allows duplicates, indexable."
tuple_info = "Tuple: ordered, immutable, allows duplicates, indexable."
set_info = "Set: unordered, mutable, no duplicates, not indexable."

print(
    f"{string_info}\n"
    f"{list_info}\n"
    f"{tuple_info}\n"
    f"{set_info}"
)

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people."
splits = sentence.split(" ")
unique_words = set(splits)
print(f"There are {len(unique_words)} unique words in the sentence: {sentence}\nWords: {unique_words}")