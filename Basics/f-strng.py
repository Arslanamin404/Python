names = ["Arsalan", "Sheezan", "Muneeb", "Farhan", "Burhan", "Musaib", "Zain", "Faizan"]
sender = "Generative Bot"
for i in range(len(names)):
    message = f"Your name is {names[i]} and this message has been sent to you by {sender}"
    print(message)

price = 23.5454054505
text = f"\n.2f will print only 2 numbs after decimal.\nYou have to pay only {price: .2f} Dollars"
print(text)
