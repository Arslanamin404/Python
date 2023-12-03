# it is similar to switch case in C, C++, Java
print("Please Select An Action --->")
print("1.Add Task\n2.Mark as Complete\n3.Remove Task\n4.Exit")
choice = int(input("\nEnter your choice: "))

match choice:
    case 1:
        print("Task Added Successfully")
    case 2:
        print("Task marked as complete")
    case 3:
        print("Task removed successfully")
    case 4:
        print("Exiting. . ..")
    case _:  # default case
        print("Invalid Choice. Please try again. . .")
