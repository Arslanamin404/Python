import requests


def getData():
    try:
        url = f"https://v2.jokeapi.dev/joke/Programming,Dark?amount=10"
        response = requests.get(url)
        data = response.json()
        return data
    except requests.RequestException as err:
        print(f"Error occurred: {err}")
        return None
    except Exception as e:
        print(f"Error! something unexpected occurred: {e}")
        return None


def displayData(joke_data):
    try:
        if joke_data is None:
            print("Failed to fetch the data!")
        else:
            # Ensure jokes is a list or an empty list if not found
            jokes = joke_data.get('jokes')
            for joke in jokes:
                category = joke.get('category')
                setup = joke.get('setup')
                deliver = joke.get('delivery')
                joke = f"{setup} {deliver}"
                print(f"Category: {category}")
                print(f"Joke: {joke}")
                print("---------------------------------------------------------------------------------------------------------------------")
    except Exception as err:
        print(f"Error! Something unexpected occurred: {err}")


if __name__ == "__main__":
    jokes = getData()
    displayData(jokes)