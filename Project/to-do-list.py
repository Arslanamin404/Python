import os


def menu():
    print("Please select an action---->\n")
    print("1. Add a To-Do item")
    print("2. View To-Do List")
    print("3. Mark an item as complete")
    print("4. Delete an item")
    print("5. Quit")


def addItem(items):
    try:
        num_items = int(input("\nNumber of items: "))
        i = 1
        for item in range(num_items):
            item_name = input(f"Enter a To-Do item {i}: ")
            items.append(item_name)
            print(f"\n'{item_name}' added to To-Do list successfully!\n")
            i += 1
    except ValueError:
        print("Error: Please enter a valid integer.")
    except Exception as e:
        print(f"Something unexpected has occurred: {e}")


def viewList(items):
    if not items:
        print("To-Do list is empty.")
    else:
        i = 1
        for item in items:
            print(f"{i}. {item}")
            i += 1


def markComplete(items):
    if not items:
        print("To-Do list is empty. Nothing to mark as complete.")
    else:
        viewList(items)
        try:
            index = int(input("\nEnter the item number to mark as complete: "))
            if 1 <= index <= len(items):
                if "✅" in items[index - 1]:
                    print("Item already marked as complete")
                else:
                    items[index - 1] = f"{items[index - 1]} ✅"
                    print(f"'{items[index - 1]}' marked as complete successfully.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"Something unexpected has occurred: {e}")


def deleteItem(items):
    if not items:
        print("To-Do list is empty. Nothing to delete.")
    else:
        viewList(items)
        try:
            index = int(input("\nEnter the item number to delete: "))
            if 1 <= index <= len(items):
                deleted_item = items.pop(index - 1)
                print(f"'{deleted_item}' deleted successfully.")
            else:
                print("Invalid item number.")
        except ValueError:
            print("Error: Please enter a valid integer.")
        except Exception as e:
            print(f"Something unexpected has occurred: {e}")


if __name__ == "__main__":
    print("Welcome to To-Do-List console app\n")
    listItems = []
    user_choice = None  # initialize user choice to none

    while True:
        os.system('cls') if os.name == 'nt' else 'clear'
        menu()
        try:
            user_choice = int(input("\nPlease enter your choice [1/2/3/4/5]: "))
        except ValueError:
            print("Error: Please enter a valid integer.")
            break
        except Exception as err:
            print(f"Something unexpected has occurred: {err}")
            break
        match user_choice:
            case 1:
                addItem(listItems)
                input("\nPress ENTER Key to continue. . .")
            case 2:
                print("\n############################################################################################")
                print("\t\t\t\tList of ITEMS")
                print("############################################################################################")
                viewList(listItems)
                input("\nPress ENTER Key to continue. . .")
            case 3:
                markComplete(listItems)
                input("\nPress ENTER Key to continue. . .")
            case 4:
                deleteItem(listItems)
                input("\nPress ENTER Key to continue. . .")
            case 5:
                print("\n####################################################################")
                print("\t\t\tExiting. . .")
                print("####################################################################")
                break
            case _:
                print("Invalid choice. Please try again. . .")
