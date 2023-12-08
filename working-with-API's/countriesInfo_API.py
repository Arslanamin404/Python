import requests
from colorama import Fore


def getData(country):
    try:
        url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
        response = requests.get(url)
        country_data = response.json()
        return country_data
    except requests.RequestException as err:
        print(f"{Fore.RED}Error occurred: {err} {Fore.RESET}")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error! something unexpected occurred: {e}{Fore.RESET}")
        return None


def displayData(data):
    try:
        if data is None:
            print(f"{Fore.RED}Error: Failed to fetch the data! {Fore.RESET}")
        else:
            print(f"Common Country Name: {data[0]['name']['common']}")
            print(f"Official Country Name: {data[0]['name']['official']}")
            print(f"Independent: {data[0]['independent']}")
            print(f"Un Member: {data[0]['unMember']}")
            print(f"Capital: {data[0]['capital'][0]}")
            print(f"Region: {data[0]['region']}")
            print(f"Sub-Region: {data[0]['subregion']}")
            print(f"Population: {data[0]['population']}")
            print(f"Time Zone: {data[0]['timezones'][0]}")

    except Exception as err:
        print(f"{Fore.RED}Error! Something unexpected occurred: {err} {Fore.RESET}")


if __name__ == "__main__":
    print("###################################################################################################")
    print("\t\t\t\t\tCountry Information")
    print("###################################################################################################\n")
    print("----------------------------------------------------------------------------------------------------")
    while True:
        country_name = input("Enter country name: ").lower()
        print("----------------------------------------------------------------------------------------------------")
        countryData = getData(country_name)
        displayData(countryData)
        print("----------------------------------------------------------------------------------------------------")
        while True:
            print("Do you want to check again? [yes/no]")
            choice = input("Enter your choice: ").lower()
            if choice not in ['yes', 'no']:
                print(
                    f"\n {Fore.RED}Error: Invalid input please enter Yes to continue or No to exit!{Fore.RESET}\n")
            else:
                break
        print("--------------------------------------------------------------------------------------------------------------")
        if choice == "no":
            print("#########################################################################################################")
            print("\t\tThank you for using our CLI Country Information Generator Application.\n\t\tWe sincerely hope you had a pleasant experience and encountered no issues.")
            print("\t\t\t\tRegards: Mohammad Arsalan Rather")
            print("\t\t\t\t\t Exiting. . .")
            print("#########################################################################################################")
            break
