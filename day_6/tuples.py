# Day 6 - 30DaysOfPython Challenge

# Exercises: Level 1

tpl = ()
sisters = ("Mar", "Maria", "Montse")
brothers = ("Marcel", "Martí")
siblings = sisters + brothers

print(f"I have {len(siblings)} siblings")

parents = ("Mario", "Montse")

family_members = siblings + parents
print(f"My family members are: {family_members}")

# Exercises: Level 2

siblings = family_members[:-2]
parents = family_members[-2:]

fruits = ("apple", "banana", "orange", "kiwi")
vegetables = ("carrot", "broccoli", "spinach")
animal_products = ("milk", "cheese", "eggs")

food_stuff_tp = fruits + vegetables + animal_products

print(f"Food stuff tuple: {food_stuff_tp}")

food_stuff_ls = list(food_stuff_tp)

middle_food = food_stuff_ls[len(food_stuff_ls) // 2]

print(f"The middle food is {middle_food}")

# Slice out the first three items and the last three items from food_stuff_lt list
first_slice = food_stuff_ls[:3]
last_slice = food_stuff_ls[-3:]

print(f"The first slice is {first_slice}\nThe second slice is {last_slice}")

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print(f"Is Estonia a nordic country? {'Estonia' in nordic_countries}")
print(f"Is Iceland a nordic country? {'Iceland' in nordic_countries}")