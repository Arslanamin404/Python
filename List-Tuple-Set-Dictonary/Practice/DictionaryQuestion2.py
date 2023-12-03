""""
Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the state in which they live.
Print each piece of information stored in your dictionary.
"""
person = {
    "First_Name": "Mohammad Arsalan",
    "Last_Name": "Rather",
    "Age": 19,
    "State": "Kashmir"
}
for key, value in person.items():
    print(f"{key} : {value}")
