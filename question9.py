import requests
from bs4 import BeautifulSoup
import csv

url = "https://en.wikipedia.org/wiki/Machine_learning"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

content = soup.find("div", id="mw-content-text")

all_tables = content.find_all("table")

target_table = None
for i in all_tables:
    rows = i.find_all("tr")
    data_rows = [row for row in rows if row.find_all("td")]
    if len(data_rows) >=3:
        target_table = i
        break

header_cells = target_table.find_all("th")
if header_cells == True:
    headers = [th.get_text(strip=True) for th in header_cells]
else:
    first_row = target_table.find("tr").find_all("td")
    headers = [f"col{i+1}" for i in range(len(first_row))]

rows_data = []
for i in target_table.find_all("tr"):
    cells = i.find_all(["td", "th"])
    row_text = [cell.get_text(strip=True) for cell in cells]

    while len(row_text) < len(headers):
        row_text.append("")
    rows_data.append(row_text[:len(headers)])

file = open("wiki_table.csv", "w", newline="")
writer = csv.writer(file)
writer.writerow(headers)

for i in rows_data:
    full = False
    for j in i:
        if j != "":
            full = True
            break
    if full == True:
        writer.writerow(i)

file.close()

print(f"number of rows: {len(rows_data)}")