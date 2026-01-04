import requests

url = "https://quotes.toscrape.com"


response = requests.get(url)


print("Status Code:", response.status_code)


print(response.text[:500])

from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
print("Page Title:", soup.title.text)


quotes = soup.find_all("div", class_="quote")
quotes_data = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    quotes_data.append([text, author])


for q in quotes_data:
    print("Quote:", q[0])
    print("Author:", q[1])
    print("-" * 40)

import pandas as pd

df = pd.DataFrame(quotes_data, columns=["Quote", "Author"])
df.to_csv("quotes.csv", index=False, encoding="utf-8")

print(" Quotes saved successfully to quotes.csv")
