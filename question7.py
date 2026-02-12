import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"
wiki = requests.get(url)
soup = BeautifulSoup(wiki.text, "html.parser")

##I had trouble with the wiki servers, I tried researching how to solve this issue and its leading me to tedious and unnecessary work.
#this seemed to do the trick:
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
#And I proceed to use this block throughout the rest of this assignment

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title.get_text())
website_content = soup.find("div", id="mw-content-text")

if website_content is None:
    print("Could not find main content!")
    exit()

paragraphs = website_content.find_all("p")

for i in paragraphs:
    text = i.get_text().strip()
    if len(text) >=50:
        print(text)
        break