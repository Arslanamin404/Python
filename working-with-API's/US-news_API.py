import requests

language = 'en'  # Language (English)


def getNews(query):
    try:

        API_key = "57f291c42c624c2cbbe657de20a56a4c"
        url = f"https://newsapi.org/v2/everything?q={query}a&from=2023-08-18&sortBy=popularity&apiKey={API_key}&language={language}"
        response = requests.get(url)
        news_data = response.json()
        return news_data
    except requests.RequestException as err:
        print(f"Error occurred: {err}")
        return None
    except Exception as e:
        print(f"Error! something unexpected occurred: {e}")
        return None


def display_news(news):
    try:
        if news is None:
            print("Failed to fetch the data!")
        else:
            # Extract source names or titles using list comprehension method
            source_names = [name['source']['name'] for name in news['articles']]
            titles = [title['title'] for title in news['articles']]
            descriptions = [description['description']for description in news['articles']]
            publishedTimings = [publishedAt['publishedAt']for publishedAt in news['articles']]

            # Print the extracted data
            for source, title, description, publishTime in zip(source_names, titles, descriptions, publishedTimings):
                print(f"Source: {source}")
                print(f"Title: {title}")
                print(f"Description: {description}")
                print(f"Published at: {publishTime}")
                print("----------------------------------------------------------------------------------------\n")
    except Exception as err:
        print(f"Error! Something unexpected occurred: {err}")


if __name__ == '__main__':
    keyword = input("Search NEWS by keyword: ")
    data = getNews(keyword)
    display_news(data)
