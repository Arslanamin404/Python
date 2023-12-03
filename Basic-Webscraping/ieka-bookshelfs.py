from bs4 import BeautifulSoup
import requests
import pandas as pd

# Create Dictionary for dataFrame
data = {
    "Product Name": [],
    "Description": [],
    "Measurement": [],
    "Price": []
}

totalPages = 10

# Step 01
Base_url = "https://www.ikea.com/us/en/cat/bookcases-10382/?page="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}

# Step 02
for pageNumber in range(1, totalPages + 1):
    url = Base_url + str(pageNumber)
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 03
    bookShelf_name = soup.find_all("span", class_="pip-header-section__title--small notranslate")
    bookShelf_description = soup.find_all("span", class_="pip-header-section__description-text")
    bookShelf_size = soup.find_all("span", class_="pip-header-section__description-measurement")
    bookShelf_price = soup.find_all("span", class_="pip-price__integer")

    # Step 04
    print(f"Page Number: {pageNumber}")
    for name, description, size, price in zip(bookShelf_name, bookShelf_description, bookShelf_size, bookShelf_price):
        data["Product Name"].append(name.text)
        data["Description"].append(description.text)
        data["Measurement"].append(size.text)
        data["Price"].append(price.text)

# Step 05
df = pd.DataFrame.from_dict(data)
print(df)
df.to_excel("ikea-bookshelf.xlsx", index=False)
