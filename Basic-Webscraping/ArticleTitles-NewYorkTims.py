import pandas as pd
from bs4 import BeautifulSoup
import requests

data = {
    "S.no": [],
    "Article Title": []
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def getArticleName():
    try:
        url = "https://www.nytimes.com"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("div", class_="css-xdandi")
        for i, article in enumerate(articles, start=1):
            data["S.no"].append(i)
            data["Article Title"].append(article.text)
    except requests.RequestException as e:
        print(f"Some error occurred: {e}")
    except Exception as e:
        print(f"Something unexpected occurred: {e}")


if __name__ == '__main__':
    print("Sit tight as we gather the data you need. Your wait won't be long, and we appreciate your patience. . .\n")
    try:
        getArticleName()
        df = pd.DataFrame.from_dict(data)
        # print(df)
        df.to_excel(
            "Basic-Webscraping\ArticleTitles-NewYorkTims.xlsx", index=False)
    except Exception as err:
        print(f"Something unexpected occurred: {err}")
    else:
        print("Record saved successfully!")