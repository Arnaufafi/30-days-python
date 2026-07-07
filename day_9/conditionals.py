# Day 9 - 30DaysOfPython Challenge

#Exercises: Level 1
#Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.

user_age = int(input("Enter your age: "))

if user_age >= 18 :
    print("You are old enough to learn to drive")
else:
    print(f"You need {18 - user_age} more years to learn to drive")

# Compare the values of my_age and your_age using if … else. Who is older (me or you)? 
# Use input(“Enter your age: ”) to get the age as input. 
# You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, 
# and a custom text if my_age = your_age. Output:

my_age = 21
your_age = int(input("Enter your age: "))
if (your_age > my_age):
    print(f"You are {your_age - my_age} years older than me.")
elif (your_age < my_age):
    print(f"You are {my_age - your_age} years younger than me.")
else:
    print("We are the same age")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, 
# if a is less b return a is smaller than b, else a is equal to b. Output:

a = int(input("Enter number one: "))
b = int(input("Enter num two: "))

if (a > b):
    print(f"{a} is grater than {b}")
elif (a < b):
    print(f"{a} is smaller than {b}")
else:
    print(f"{a} is equal to {b}")

# Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:

score = int(input("Introduce your score: "))

if (score >= 90):
    print("Your grade is A")
elif (score >= 80):
    print("Your grade is B")
elif (score >= 70):
    print("Your grade is C")
elif (score >= 60):
    print("Your grade is D")
else:
    print("Your grade is F")


# Get the month from user input then check if the season is Autumn, Winter, Spring or Summer. 
# If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. March, April or May, the season is Spring 
# June, July or August, the season is Summer

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July", "August"]

user_season = input("Enter a month: ")

if user_season in autumn:
    print("The season is autumn")
elif user_season in winter:
    print("The season is winter")
elif user_season in spring:
    print("The season is spring")
elif user_season in summer:
    print("The season is summer")
else:
    print("Invalid month")

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')

fruits = ['banana', 'orange', 'mango', 'lemon']

user_fruit = input("Enter a fruit: ")
if (user_fruit in fruits):
    print(f"That fruit ({user_fruit}) already exist in the list")
else:
    fruits.append(user_fruit)
    print(fruits)

# Exercises: Level 3

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.

if ("skills" in person and person["skills"]):
    skills = list(person["skills"])
    middle = len(skills) // 2
    print(f"{skills[middle]}")
else:
    print("No skills found")

# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.

if ("skills" in person and person["skills"]):
    skills = list(person["skills"])
    if ("Python" in skills):
        print("Person has Python skill")
    else:
        print("Person doesn't have Python skill")
else:
    print("No skills found")

# If a person skills has only JavaScript and React, print('He is a front end developer'), 
# if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
# if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
# else print('unknown title') - for more accurate results more conditions can be nested!

front = ["JavaScript", "React"]
back = ["Node", "Python", "MongoDB"]
full = ["React", "Node", "MongoDB"]

skills = list(person["skills"])

if all(skill in skills for skill in front):
    print("Front-end developer")
elif all(skill in skills for skill in back):
    print("Back-end developer")
elif all(skill in skills for skill in full):
    print("Full-stack developer")
else:
    print("Unknown skill set")

# option two

skills = set(person["skills"])

if set(front).issubset(skills):
    print("Front-end developer")
elif set(back).issubset(skills):
    print("Back-end developer")
elif set(full).issubset(skills):
    print("Full-stack developer")

# If the person is married and if he lives in Finland, print the information in the following format:

if (person["is_married"] == True and person["country"] == "Finland"):
    print(f"{person['first_name']} lives in Finland. He is married")
    