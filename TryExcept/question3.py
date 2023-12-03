cities = {
    "Tokyo": {
        "Country": "Japan",
        "Population": "13 million",
        "Fact": "Tokyo is known for its incredibly efficient public transportation system, including the world-famous Shinkansen (bullet train) network."
    },
    "Paris": {
        "Country": "France",
        "Population": "Over 2 million",
        "Fact": "Paris is often called the 'City of Love' and is renowned for its romantic ambiance, iconic landmarks like the Eiffel Tower, and its rich cultural heritage."
    },
    "New York": {
        "Country": "USA",
        "Population": "Over 8 million",
        "Fact": "New York City is home to the Statue of Liberty, a gift from France, symbolizing freedom and democracy, and has been a welcoming symbol to immigrants for over a century."
    },
    "Sydney": {
        "Country": "Australia",
        "Population": "Over 5 million",
        "Fact": "Sydney is famous for its stunning natural harbor and the Sydney Opera House, a UNESCO World Heritage Site and one of the most recognizable architectural landmarks in the world."
    },
    "Cairo": {
        "Country": "Egypt",
        "Population": "Over 9 million",
        "Fact": "Cairo is home to the Great Pyramids of Giza, one of the Seven Wonders of the Ancient World, and the Sphinx, which has captured the imagination of people for centuries."
    },
    "Moscow": {
        "Country": "Russia",
        "Population": "Over 12 million",
        "Fact": "Moscow's Red Square is not only a historical and political center but also the location of St. Basil's Cathedral, known for its unique and colorful onion domes."
    },
    "Cape Town": {
        "Country": "South Africa",
        "Population": "Over 4 million",
        "Fact": "Cape Town is famous for its stunning natural beauty, including Table Mountain, which offers panoramic views of the city and the surrounding coastline."
    },
    "Istanbul": {
        "Country": "Turkey",
        "Population": "Over 15 million",
        "Fact": "Istanbul straddles two continents, Europe and Asia, and is known for its rich history, with iconic landmarks like the Hagia Sophia and the Blue Mosque."
    },
}

print("These are the list of cities enter any city name to get its details:")
print("-----------------------------------------------------------------------------------------------------------")
for city in cities.keys():
    print(city, end="\t\t")
print("\n-----------------------------------------------------------------------------------------------------------")

try:
    userInput = input("\nEnter City: ").title()
    print("-------------------")
    found = False
    for city, cityInfo in cities.items():
        if userInput == city:
            found = True
            for key, value in cityInfo.items():
                print(f"{key}: {value}")
        if not found:
            raise ValueError("City not found!")
except ValueError as err:
    print(f"Error occurred: {err}")
except Exception as err:
    print(f"An unexpected error has occurred: {err}")
