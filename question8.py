import requests
from bs4 import BeautifulSoup

##I am having trouble with the wiki servers, I tried researching how to solve this issue and its leading me to tedious and unnecessary work.

url = "https://en.wikipedia.org/wiki/Data_science"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
content = soup.find("div", id = "mw-content-text")

if content is None:
    print("Could not find main content!")
    exit()

headings = content.find_all("h2")

exclude = ["References", "External links", "See also", "Notes"]
clean_headings = []

for i in headings:
    heading_text = i.get_text().strip()
    heading_text = heading_text.replace("[edit]", "").strip()

    skip = False
    for word in exclude:
        if word in heading_text:
            skip = True
            break
    if skip:
        continue

    clean_headings.append(heading_text)

file = open("headings.txt", "w")

for heading in clean_headings:
    file.write(heading + "\n")

file.close()