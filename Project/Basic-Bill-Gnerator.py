# WAP which will keep adding numbers inputted by user, until user press 'q'
import pandas as pd

bill = {
    "Item Name": [],
    "Price": []
}

total = 0
print("###################################################################################################################################")
print("\tWelcome, in this program you will be asked to enter the name of the item and then price of that item.")
print("###################################################################################################################################\n")
print(">> To EXIT and generate the total bill enter 'q' and then hit enter on your keyboard!")
while True:
    try:
        itemName = input("\nEnter Item name (q):").lower()
        if itemName != 'q':
            itemPrice = float(input("Item price: "))
            bill["Item Name"].append(itemName.title())
            bill["Price"].append(itemPrice)
            total += itemPrice
        else:
            break
    except ValueError as err:
        print("\nPlease enter a valid price. . .\n")
    except Exception as e:
        print(f"Something unexpected occurred: {e}")

print("\n\n\t\tBILL SUMMARY")
print("---------------------------------------------------------------------------------------")
df = pd.DataFrame.from_dict(bill)
df.index = range(1, len(df) + 1)
print(df)
print("---------------------------------------------------------------------------------------")
print(f"Total Payable Amount = {total}")
print("---------------------------------------------------------------------------------------\n")
print("\n###############################################################################################################################################")
print("Thank you for choosing our store for your shopping needs. We sincerely hope you had a pleasant experience and encountered no issues.")
print("\t\t\t\t\tWe look forward to serving you again in the future.")
print("\t\t\t\t\t\tBest regards, Mohammad Arsalan Rather")
print("###############################################################################################################################################")
