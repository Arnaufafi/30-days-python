# Day 20 - 30DaysOfPython Challenge

import requests
import re
import statistics

# Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

response = requests.get(romeo_and_juliet)
print(response)

def find_most_frequent_words(text, amount):

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    words_count = {}
    for word in words:
        if word not in words_count:
            words_count[word] = 0
        words_count[word] += 1

    sorted_words = sorted(words_count.items(), key=lambda x:x[1], reverse=True)
    return sorted_words[:amount]

print(f"The most frequent words in the url are: {find_most_frequent_words(response.text, 10)}")

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
cats_api = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(cats_api)
cats = response.json()
# print(cats[0]) to see structure

# the min, max, mean, median, standard deviation of cats' weight in metric units.
weights = []

for cat in cats:
    metric_weight = cat["weight"]["metric"]
    numbers = metric_weight.split("-")
    numbers = list(map(float, numbers))
    avg_weight = sum(numbers)/len(numbers)
    weights.append(avg_weight)

print("Cats' weight in metric units")
print("Min:", min(weights))
print("Max:", max(weights))
print("Mean:", statistics.mean(weights))
print("Median:", statistics.median(weights))
print("Standard deviation", statistics.stdev(weights))

# the min, max, mean, median, standard deviation of cats' lifespan in years.
life = []

for cat in cats:
    lifespan = cat["life_span"]
    numbers = lifespan.split("-")
    numbers = list(map(float, numbers))
    avg_life = sum(numbers) / len(numbers)
    life.append(avg_life)

print("Cats lifespan in years")
print("Min:", min(life))
print("Max:", max(life))
print("Mean:", statistics.mean(life))
print("Median:", statistics.median(life))
print("Standard deviation", statistics.stdev(life))

# Create a frequency table of country and breed of cats

freq = {}

for cat in cats:
    country = cat["origin"]
    breed = cat["name"]
    if country not in freq:
        freq[country] = set()
    if breed != None: 
        freq[country].add(breed)

print(freq)

# APIs not updated for the next ex