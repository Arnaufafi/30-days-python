# Day 19 - 30DaysOfPython Challenge

import json
import re
import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from stopwords import stopwords

# Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def count_lines_and_words(file):
    text = file.read()
    lines = text.splitlines()
    words = text.split()

    return len(lines), len(words)


# Read obama_speech.txt file and count number of lines and words
f = open("day_19\speech\obama_speech.txt")
lines, words = count_lines_and_words(f)
print(f"Obama speech has {lines} lines and {words} words")
f.close()

# Read michelle_obama_speech.txt file and count number of lines and words
f = open("day_19\speech\michelle_obama_speech.txt")
lines, words = count_lines_and_words(f)
print(f"Michelle Obama speech has {lines} lines and {words} words")
f.close()

# Read donald_speech.txt file and count number of lines and words
f = open("day_19\speech\donald_speech.txt")
lines, words = count_lines_and_words(f)
print(f"Trump speech has {lines} lines and {words} words")
f.close()

# Read melina_trump_speech.txt file and count number of lines and words
f = open("day_19\speech\melina_trump_speech.txt")
lines, words = count_lines_and_words(f)
print(f"Melina speech has {lines} lines and {words} words")
f.close()

# Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages

def most_spoken_languages(filename, amount):

    with open(filename, "r", encoding="utf-8") as f:
        countries_dct = json.load(f)

    spoken_languages = {}

    for country in countries_dct:
        for language in country["languages"]:
            if language not in spoken_languages:
                spoken_languages[language] = 0
            spoken_languages[language] += 1

    spoken_languages_sorted = sorted(spoken_languages.items(), key=lambda x: x[1], reverse=True)
    return spoken_languages_sorted[:amount]

print(most_spoken_languages('day_19\countries\countries_data.json', 3))

# Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries

def most_populated_countries(filename, amount):

    with open(filename, "r", encoding="utf-8") as f:
        countries_dct = json.load(f)

    countries_dct = [{"name": c["name"], "population": c["population"]} for c in countries_dct]
    populated_countries_sorted = sorted(countries_dct, key=lambda x: x["population"], reverse=True)
    return populated_countries_sorted[:amount]


print(most_populated_countries('day_19\countries\countries_data.json',10))


## LEVEL 2

# Extract all incoming email addresses as a list from the email_exchange_big.txt file.

with open("day_19/email/email_exchanges_big.txt", "r", encoding="utf-8") as f:
    text = f.read()

email_adr = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9._%+-]+\.[a-zA-Z]{2,}", text)
print(email_adr[:3])
print(len(email_adr), "emails found")

# Use the function, find_most_frequent_words to find
def find_most_frequent_words(filename, amount):
    with open(filename, "r", encoding="utf-8") as f:
        text = f.read()

    words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
    words_count = {}
    for word in words:
        if word not in words_count:
            words_count[word] = 0
        words_count[word] += 1

    sorted_words = sorted(words_count.items(), key=lambda x:x[1], reverse=True)
    return sorted_words[:amount]


# The ten most frequent words used in Obama's speech
print(find_most_frequent_words("day_19\speech\obama_speech.txt",10))

# The ten most frequent words used in Michelle's speech
print(find_most_frequent_words("day_19\speech\michelle_obama_speech.txt",10))

# The ten most frequent words used in Trump's speech
print(find_most_frequent_words("day_19\speech\donald_speech.txt",10))

# The ten most frequent words used in Melina's speech
print(find_most_frequent_words("day_19\speech\melina_trump_speech.txt",10))


# Write a python application that checks similarity between two texts. 
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
# For instance check the similarity between the transcripts of Michelle's and Melina's speech.
# You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) 
# and finally to check the similarity(check_text_similarity). 
# List of stop words are in the data directory

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Záéíóúüñ\s]", " ", text)
    text = re.sub(r"\s+", " ",text).strip()
    return text

def remove_support_words(text, stopwords):
    words = text.split()
    filtered = [w for w in words if w not in stopwords]
    return " ".join(filtered)

def similarity(text1, text2):
    vect = TfidfVectorizer().fit([text1,text2])
    tfidf = vect.transform([text1,text2])
    return cosine_similarity(tfidf[0], tfidf[1])[0][0]

def bag_similarity(text1, text2):
    w1 = set(text1.lower().split())
    w2 = set(text2.lower().split())
    return len(w1 & w2) / len(w1 | w2)

def load_text(text_or_file):
    try:
        with open(text_or_file, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return text_or_file

def check_text_similarity(text1, text2, stopwords):

    t1 = load_text(text1)
    t2 = load_text(text2)

    #clean
    t1 = clean_text(t1)
    t2 = clean_text(t2)

    #remove stopwords
    t1 = remove_support_words(t1, stopwords)
    t2 = remove_support_words(t2, stopwords)

    #similarities
    tfidf_sim = similarity(t1,t2)
    bag_sim = bag_similarity(t1,t2)

    return {
        "tfidf_similarity": tfidf_sim,
        "bag_similarity": bag_sim
    }

result = check_text_similarity(
    "day_19/speech/michelle_obama_speech.txt",
    "day_19/speech/melina_trump_speech.txt",
    stopwords
)

print(result)

# Find the 10 most repeated words in the romeo_and_juliet.txt

print(find_most_frequent_words("day_19/speech/romeo_and_juliet.txt",10))

# Read the hacker news csv file and find out:
# Count the number of lines containing python or Python
# Count the number lines containing JavaScript, javascript or Javascript
# Count the number lines containing Java and not JavaScript

count_python = 0
count_js = 0
count_java_njs = 0

with open("day_19/csv/hacker_news.csv", "r", encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    next(csv_reader)  # saltar cabecera

    for row in csv_reader:
        line = " ".join(row).lower()

        # python
        if "python" in line:
            count_python += 1

        # javascript
        elif "javascript" in line:
            count_js += 1

        # java pero NO javascript
        elif "java" in line and "javascript" not in line:
            count_java_njs += 1

print("Lines containing Python:", count_python)
print("Lines containing JavaScript:", count_js)
print("Lines containing Java (not JavaScript):", count_java_njs)