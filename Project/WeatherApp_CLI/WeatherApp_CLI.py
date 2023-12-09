import requests
import json
from dotenv import load_dotenv
import os
# Website = https://www.weatherapi.com/api-explorer.aspx

load_dotenv()


def get_weather(location):
    url = f"http://api.weatherapi.com/v1/current.json?key={os.getenv('API_KEY')}&q={location}&aqi=no"
    try:
        data_dict = requests.get(url).json()  # this method is proffered
        return data_dict
    except requests.RequestException as err:
        print(f"Error occurred: {err}")
        return None
    except Exception as err:
        print(f"Something unexpected occurred: {err}")
        return None


def display_weather(weather_data):
    try:
        if weather_data is None:
            print("Unable to fetch weather data! Please try again later.")
        else:
            # use single quotes bex we are dealing with json
            print(f"- Weather in {weather_data['location']['name']}")
            print(f"- Region: {weather_data['location']['region']}")
            print(f"- Country: {weather_data['location']['country']}")
            print(f"- Temperature(C): {weather_data['current']['temp_c']} C")
            print(f"- Temperature(F): {weather_data['current']['temp_f']} F")
            print(f"- Humidity: {weather_data['current']['humidity']}")
            print(
                f"- Current Condition: {weather_data['current']['condition']['text']}")
    except Exception as err:
        print(f"Error! something unexpected occurred: {err}")


if __name__ == "__main__":
    print("###############################################################################################################################")
    print("\t\t\t\t\t\tWEATHER-CHECK CLI Application")
    print("###############################################################################################################################\n")
    while True:
        region = input("Enter city or state: ")
        print("--------------------------------------------------------------------------------------------------------------")
        data = get_weather(region)
        display_weather(data)
        print("--------------------------------------------------------------------------------------------------------------")
        print("Do you want to check weather again? [yes/no]")
        choice = input("Enter your choice: ").lower()
        print("--------------------------------------------------------------------------------------------------------------")
        if choice == "no":
            print("#########################################################################################################")
            print("\t\t\tThank you for using our CLI Weather Application.\n \tWe sincerely hope you had a pleasant experience and encountered no issues.")
            print("\t\t\t\tRegards: Mohammad Arsalan Rather")
            print("\t\t\t\t\t Exiting. . .")
            print("#########################################################################################################")
            break
