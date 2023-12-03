import pandas
import pandas as pd
from bs4 import BeautifulSoup
import requests

data = {
    "Movie Name": [],
    "Rating": []
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def movieScraping():
    url = "https://www.imdb.com/chart/top/?sort=rank%2Casc"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    data_table = soup.find("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-3f13560f-0 sTTRj compact-list-view ipc-metadata-list--base")

    names = data_table.find_all("h3", class_="ipc-title__text")
    rating = data_table.find_all("span",class_="ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating")

    for name, rate in zip(names, rating):
        data["Movie Name"].append(name.text)
        data["Rating"].append(rate.text)


movieScraping()
df = pd.DataFrame.from_dict(data)
df.to_excel("imbd-Movies.xlsx", index=False)
# print(df)
