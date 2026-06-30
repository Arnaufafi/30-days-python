# Day 4 - 30DaysOfPython Challenge

# Concatenate the string

space = " "
concatenated_string = "Thirty" + space + "Days" + space + "Of" + space + "Python"
print(concatenated_string)
concatenated_string = "Coding" + space + "For" + space + "All"
print(concatenated_string)

# Printing length and modifing a string

company = "Coding For All"
print(company)
company_len = len(company)
print(company_len)
company_upper = company.upper()
print(company_upper)
company_lower = company.lower()
print(company_lower)
company_capitalize = company.capitalize()
print(company_capitalize)
company_title = company.title()
print(company_title)
company_swapcase = company.swapcase()
print(company_swapcase)

# Cut(slice) out the first word of Coding For All string.

company_cut = company[7:]
print(company_cut)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

print(f"Check if Coding For All string contains a word Coding using the method index: {company.index('Coding')} (0 == True)\n")

# Replace
company_replace = company.replace("Coding", "Python")
print(f"Relplace Coding to Python: {company} --> {company_replace}\n")

python_sentence = "Python for Everyone"
python_replace = python_sentence.replace("Everyone","All" )
print(f"Relplace Everyone to All: {python_sentence} --> {python_replace}\n")

# Split the string 'Coding For All' using space as the separator (split()) .
sentence_coding = "Coding For All"
split_string = sentence_coding.split(" ")
print(f"Firts word: {split_string[0]}, Second word: {split_string[1]}, Third word: {split_string[2]}\n")

split_string = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(",")
print(f"Firts word: {split_string[0]}, Second word: {split_string[1]}, Third word: {split_string[2]}\n")

# What is the character at index 0 in the string Coding For All.
print(f"The character 1 at {sentence_coding} is {sentence_coding[0]} and last index is {len(sentence_coding) - 1} \n")
print(f"The character 9 at {sentence_coding} is {sentence_coding[10]} \n")


# Acronym
acronym = "".join(word[0] for word in python_sentence.split())
print(f"{acronym} = {python_sentence}")
acronym = "".join(word[0] for word in sentence_coding.split())
print(f"{acronym} = {sentence_coding} \n")

# Index

index_C = sentence_coding.index("C")
print(f"The index of C in {sentence_coding} is {index_C}")
index_F = sentence_coding.index("F")
print(f"The index of F in {sentence_coding} is {index_F}")
index_l = sentence_coding.rfind("l")
print(f"The index of last l in {sentence_coding} is {index_l}")
because_sentence = "You cannot end a sentence with because because because is a conjunction"
print(f"The first ocurrence of the word because --> {because_sentence.find('because')} ")
print(f"The last ocurrence of the word because --> {because_sentence.rfind('because')} \n")

slice_because = because_sentence[31:47+len("because")]
print(f"Sliced because = {slice_because}")

# Does 'Coding For All' start with a substring Coding?
print(f"Does 'Coding For All' start with a substring Coding? {sentence_coding.startswith('Coding')}")

# Does 'Coding For All' end with a substring coding?
print(f"Does 'Coding For All' end with a substring coding? {sentence_coding.endswith('coding')}\n")

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.

sentence_coding_spaces = '   Coding For All      '
print(f"Remove spaces from: {sentence_coding_spaces} --> {sentence_coding_spaces.strip()}\n")

#Which one of the following variables return True when we use the method isidentifier():
print(f"30DaysOfPython is an identifier = {'30DaysOfPython'.isidentifier()}")
print(f"thirty_days_of_python is an identifier = {'thirty_days_of_python'.isidentifier()}\n")

# Join
unjoined_words = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_words = "".join(word + " " for word in unjoined_words)
print(f"Joined words: {joined_words}\n")

# Split
two_sentences = "I am enjoying this challenge.\nI just wonder what is next."
sentence_one = two_sentences.split("\n")[0]
sentence_two = two_sentences.split("\n")[1]
print(f"S1 = {sentence_one}\nS2 = {sentence_two}\n")

# Tab
print("Name\t\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# String formatting
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with {radius} is {area:.0f} meters square")

num1 = 8
num2 = 6
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {(num1/num2):.2f}")
print(f"{num1} % {num2} = {num1%num2}")
print(f"{num1} // {num2} = {num1//num2}")
print(f"{num1} ** {num2} = {num1**num2}")