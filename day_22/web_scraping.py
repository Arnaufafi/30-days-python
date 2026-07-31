# Day 21 - 30DaysOfPython Challenge

import requests
import json
from bs4 import BeautifulSoup
import os

# Scrape the following website and store the data as json file(url = 'http://www.bu.edu/president/boston-university-facts-stats/').

url = 'http://www.bu.edu/president/boston-university-facts-stats/'

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
data = {}
data["Title"] = soup.title.get_text()
data["Body"] = soup.body.get_text(separator="\n", strip=True)
data["Response"] = response.status_code

data_json = json.dumps(data, indent=4)

with open('scraped_data/ex1.json', "w", encoding="utf-8") as f:
    f.write(data_json)

# Extract the table in this url (https://archive.ics.uci.edu/dataset/53/iris) and change it to a json file

url = "https://archive.ics.uci.edu/dataset/53/iris"

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

tables = soup.find_all('table', class_='table my-4 w-full')
table = tables[0]

rows = []

for tr in table.find_all('tr'):
    cells = [td.get_text(strip=True) for td in tr.find_all(["td","th"])]
    if cells:
        rows.append(cells)

headers = rows[0]
data = []

for row in rows[1:]:
    item = dict(zip(headers,row))
    data.append(item)

data_json = (json.dumps(data, indent=4))
with open('scraped_data/ex2.json', "w", encoding="utf-8") as f:
    f.write(data_json)


# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States).
# The table is not very structured and the scrapping may take very long time.

url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

table = soup.select_one("table.wikitable.sortable")
rows = table.find_all("tr")

presidents = []
current = None

for tr in rows:
    if tr.find("img"):
        cells = tr.find_all(["th", "td"])
        texts = [c.get_text(strip=True) for c in cells]

        if current:
            presidents.append(current)
        current = {
            "No": texts[0],
            "Name": texts[2],
            "Term": texts[3],
            "Party": texts[5],
            "Election": texts[6],
            "Vice President": texts[7]
        }
    else:
        cells = tr.find_all(["td"])
        texts = [c.get_text(strip=True) for c in cells]

        if current and len(texts) == 2:
            current["Election2"] = texts[0]
            current["Vice President2"] = texts[1]
if current:
    presidents.append(current)

with open("scraped_data/ex3.json", "w", encoding="utf-8") as f:
    json.dump(presidents, f, indent=4)
