import requests


def getData(ip):
    try:
        url = f"https://ipapi.co/{ip}/json/"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data_dict = response.json()
        return data_dict
    except requests.RequestException as err:
        print(f"Error! {err}")
        return None
    except Exception as err:
        print(f"Error! {err}")
        return None


def displayData(ip_data):
    try:
        if ip_data is None:
            print("Failed to fetch the data!")
        else:
            print(f"Ip Addr: {ip_data['ip']}")
            print(f"Version: {ip_data['version']}")
            print(f"City: {ip_data['city']}")
            print(f"Region: {ip_data['region']}")
            print(f"Country: {ip_data['country_name']}")
            print(f"Currency: {ip_data['currency']}")

    except Exception as err:
        print(f"Error! Something unexpected occurred: {err}")


ipAddress = input("Enter your IP Address: ").strip()
data = getData(ipAddress)
displayData(data)
