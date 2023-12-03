import pandas as pd
from bs4 import BeautifulSoup
import requests

data = {
    "about": [],
    "news": []
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}


def scrape_news():
    try:
        url = "https://www.theguardian.com/tech"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        page = soup.find("section", class_="dcr-1sz9f2")
        names = soup.find_all("div", class_="dcr-1o7trcs")
        headlines = page.find_all("span", class_="show-underline dcr-adlhb4")

        for name, news in zip(names, headlines):
            data["about"].append(name.text)
            data["news"].append(news.text)
    except requests.RequestException as err:
        print(f"Some error occurred: {err}")
    except Exception as e:
        print(f"Something unexpected occurred: {e}")


if __name__ == '__main__':
    print("Sit tight as we gather the data you need. Your wait won't be long, and we appreciate your patience. . .\n")
    try:
        scrape_news()
        df = pd.DataFrame.from_dict(data)
        df.to_excel("theGuardians-Headlines.xlsx", index=False)
    except Exception as err:
        print(f"Something unexpected occurred: {err}")
    else:
        print("Record saved successfully!")
        input("\nPress Enter key to exit. . .")
