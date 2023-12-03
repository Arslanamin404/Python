from bs4 import BeautifulSoup
import requests
import pandas as pd

data = {
    "Laptop Name": [],
    "Price": [],
    "Specifications": [],
    "Rating": []
}
# Part 01
num_of_pages = 20

"""
A "header" in web requests is like an ID card. It tells the website who you are, like a browser or bot.
Some websites dont allow bots to access their specific data that is why we use headers
Setting up a header to mimic a web browser for a smooth request.
"""
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# this loop is for number of pages
for page_number in range(1, num_of_pages + 1):
    url = f"https://www.flipkart.com/search?q=laptop&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop&requestId=0e4e95ec-e34b-499b-ac82-4160ac7c77d2&as-backfill=on&page={str(page_number)}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # part 2
    laptop_names = soup.find_all("div", class_="_4rR01T")
    laptop_prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
    laptop_Description_ul = soup.find_all("ul", class_="_1xgFaf")
    laptop_ratings = soup.find_all("div", class_="_3LWZlK")

    # Part 3
    print(f"Page Number: {page_number}")
    for laptop, price, description_li, rating in zip(laptop_names, laptop_prices, laptop_Description_ul, laptop_ratings):
        data["Laptop Name"].append(laptop.string)
        data["Price"].append(price.text)
        data["Specifications"].append(description_li.text)
        data["Rating"].append(rating.text)

# Step 04
df = pd.DataFrame.from_dict(data)
print(df)
df.to_excel("Flipkart-Laptop-Scraping.xlsx", index=False)
