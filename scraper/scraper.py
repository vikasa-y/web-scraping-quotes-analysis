import requests
import pandas as pd
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com/"
url = base_url + "/"

all_quotes = []

while url:
    response = requests.get(url)

    soup = BeautifulSoup(response.text , "html.parser")

    print("Status Code :",response.status_code)

    quotes =soup.find_all("div" , class_="quote")


    for quote in quotes:
        text = quote.find("span" ,class_="text").text
        author = quote.find("small" ,class_="author").text

        tags = quote.find_all("a" , class_="tag") 
        tag_list = [tag.text for tag in tags]

        all_quotes.append({
            "quote": text,
            "author": author,
            "tags": tag_list
        })

        next_page = soup.find("li", class_="next")

        if next_page:
            link = next_page.find("a")
            url = base_url + link["href"]
        else:
            url = None

print("Total quotes:", len(all_quotes))
# print(all_quotes[0])
print(type(all_quotes))
print(len(all_quotes))

df = pd.DataFrame(all_quotes)

print(df.head())
print(df.shape)
print(df.info())

df.to_csv("data/raw/quotes_raw.csv", index=False)