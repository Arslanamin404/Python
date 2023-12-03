import time

# Define a Contact class to store contact information.
class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

# Define a ContactBook class to manage contacts.
class ContactBook:
    def __init__(self):
        # Initialize an empty dictionary to store contacts.
        self.contacts = {}  

    # Method to add a new contact to the contact book.
    def add_contacts(self, contact):
        self.contacts[contact.name] = contact
        print(f"\nContact {contact.name} added successfully!.\n")
        time.sleep(1)

    # Method to view all contacts in the contact book.
    def view_contacts(self):
        if not self.contacts:
            print(
                "\n------------------------------\n>> Contact Book is Empty!\n------------------------------\n")
        else:
            print("\nContact List:\n------------------")
            for index, (name, contact) in enumerate(self.contacts.items(), start=1):
                # :25 leaves 25 chars space ==> Format the output for better readability.
                print(f"{index}. {name:25}: {contact.number}")  
            print("-----------------------------------------------\n")
        time.sleep(1)

    # Method to search for a contact by name.
    def search_contact(self, name):
        if name in self.contacts:
            print(f"\n{name}'s number is: {self.contacts[name].number}.\n")
        else:
            print(f"\n{name}'s contact not found in Contact Book!\n")
        time.sleep(1)

    # Method to delete a contact by name.
    def delete_contact(self, name):
        if name in self.contacts:
            self.view_contacts()  # Display the list of contacts before deletion.
            self.contacts.pop(name)  # Remove the contact from the dictionary.
            print(f"\n{name}'s number Deleted Successfully!\n")
        else:
            print(f"\n{name}'s contact not found in Contact Book!")


# Define the main function to interact with the ContactBook.
def main():
    # Create a new instance of the ContactBook class.
    contact_book = ContactBook()  

    # Start an infinite loop for the user to interact with the ContactBook.
    while True:
        print("Please select an action --->\n")
        print("1. Add Contact\n2. View Contacts\n3. Delete Contact\n4. Search Contact\n5. Exit\n")

        try:
            # Get the user's choice as an integer.
            user_choice = int(input("Please Enter Your Choice: ")) 
        except ValueError:
            print("\n------------------------------------------------")
            print(">> Please enter a valid choice [1/2/3/4/5].")
            print("------------------------------------------------\n")
            time.sleep(1)
        except Exception as err:
            print(f"Error! Something unexpected occurred: {err}")
            break
        else:
            if user_choice == 1:
                name = input("\nEnter Name: ").title()
                number = input("Enter Number: ")
                new_contact = Contact(name, number)
                contact_book.add_contacts(new_contact)
            elif user_choice == 2:
                contact_book.view_contacts()
            elif user_choice == 3:
                if not contact_book.contacts:
                    print(
                        "\n------------------------------\n>> Contact Book is Empty!\n------------------------------\n")
                    time.sleep(1)
                else:
                    contact_book.view_contacts()
                    name = input(
                        "\nEnter Contact Name to Delete: ").title()
                    contact_book.delete_contact(name)
            elif user_choice == 4:
                if not contact_book.contacts:
                    print(
                        "\n------------------------------\n>> Contact Book is Empty!\n------------------------------\n")
                    time.sleep(1)
                else:
                    name = input("\nEnter Name: ").title()
                    contact_book.search_contact(name)
            elif user_choice == 5:
                print("\nExiting Contact Book. GoodBye!")
                time.sleep(1)
                break
            else:
                print("\nInvalid Choice. Please enter [1/2/3/4].\n")

# Entry point of the script.
if __name__ == "__main__":
    main()
