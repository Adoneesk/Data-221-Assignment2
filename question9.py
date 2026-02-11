import requests
from bs4 import BeautifulSoup

url = requests.get("https://en.wikipedia.org/wiki/List_of_Unemployment_rates")
soup = BeautifulSoup(url.text, "html.parser")

