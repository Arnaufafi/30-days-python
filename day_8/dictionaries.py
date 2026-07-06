# Day 8 - 30DaysOfPython Challenge

# Create an empty dictionary called dog
dog ={}

# Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Sky"
dog["color"] = "White"
dog["breed"] = "Labrador"
dog['legs'] = 4
dog['age'] = 3

print(dog)

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "first_name": "Josh",
    "last_name": "Smith",
    "gender": "male",
    "age": 21,
    "marital_status": "single",
    "skills": ["Python", "Java", "SQL"],
    "country": "Spain",
    "city": "Barcelona",
    "address": "Street 12"
}

# Get the length of the student dictionary
len_dict = len(student)
print(f"The length of the student dictionary is: {len_dict}\n")

# Get the value of skills and check the data type, it should be a list
skills = student["skills"]
print(f"The data type of skills is {type(skills)}\n")

# Modify the skills values by adding one or two skills
print(student["skills"])
skills.append("Machine Learning")
student["skills"] = skills
print(student["skills"])

# Get the dictionary keys as a list
student_keys = list(student.keys())
print(f"The keys are: {student_keys}\n")

# Get the dictionary values as a list
student_values = list(student.values())
print(f"The values are: {student_values}\n")

# Change the dictionary to a list of tuples using items() method
student_list = list(student.items())
print(student_list)

# Delete items in the dictionary
print(student)
student.popitem()
print(student)
student.pop("skills")
print(student)

# Delete one of the dictionaries
del student