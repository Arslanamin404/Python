from bs4 import BeautifulSoup
import requests
import pandas as pd

data = {
    "Quote": [],
    "Author": []
}

# Part 01
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


# Step 02
def scrapeQuotes(num_of_pages):
    for pageNum in range(1, num_of_pages + 1):
        url = f"https://quotes.toscrape.com/page/{str(pageNum)}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.prettify())    #this will print the HTML of website

        # Step 03
        quotes = soup.find_all("span", class_="text")
        authors = soup.find_all("small", class_="author")

        # Step 04
        for quote, author in zip(quotes, authors):
            data["Quote"].append(quote.text)
            data["Author"].append(author.text)
            # print(f"{quote.text}\n\tby {author.text}\n")


TotalPages = 10
scrapeQuotes(TotalPages)

df = pd.DataFrame.from_dict(data)
print(df)
df.to_excel("ScrapedQuotes.xlsx",index=False)
