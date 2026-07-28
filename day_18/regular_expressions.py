# Day 18 - 30DaysOfPython Challenge

import re
from collections import Counter

## LEVEL 1

# What is the most frequent word in the following paragraph?
paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
cleaned = re.sub(r'[^\w\s]', "", paragraph.lower())

words_count = {}
words = re.split(" ", cleaned)
for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] += 1

sorted_words = sorted(words_count.items(), key=lambda x: x[1], reverse=True)

print(sorted_words)

# The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. 
# Extract these numbers from this whole text and find the distance between the two furthest particles.
paragraph=" The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."
cleaned = re.findall(r'-?\d+',paragraph)
points = [int(n) for n in cleaned]
points.sort()
print(points)
distance = points[-1] - points[0]
print(f"The distance between the two furthest particles is: {distance}")

## LEVEL 2

# Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(variable_name):
    pattern = r"^[a-zA-Z_]\w*$"

    if not re.match(pattern, variable_name):
        return False

    return True

print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True

## LEVEL 3

# Clean the following text. After cleaning, count three most frequent words in the string.
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
cleaned = re.sub(r'[^a-zA-z\s]',"", sentence)
print(cleaned)
words = cleaned.lower().split()
counts = Counter(words)
print(counts.most_common(3))
