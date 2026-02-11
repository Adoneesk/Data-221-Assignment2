import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Data_science"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

title = soup.title
print(title)
website_content = soup.find("div", id="mw-content-text")
#chatgpt.com taught me what to do if the website has a possibility of changing{
if website_content is None:
    print("Could not find main content!")
    exit()
#}
paragraphs = website_content.find_all("p")

for i in paragraphs:
    text = i.get_text().strip()
    if len(text) >=50:
        print(text)
        break