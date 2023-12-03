import connection
import tdl_DAO
import model
import sys

conn = connection.MyDatabase.get_connection()
tdl_data = tdl_DAO.TDL_DAO()


def menu():
    print("============== To-DO List ==============\n")
    print("What would you like to do?")
    print("1. Add a new task")
    print("2. View tasks")
    print("3. Mark task as complete")
    print("4. Remove a task")
    print("5. Exit")


def add_task():
    task_name = input("\nEnter Task Name: ").title()
    task_desc = input("Enter Task Description: ")
    task_due_date = input("Enter Task Due Date: ").title()
    print("Is Task Completed? '1' as True and '0' as False.")
    task_isComplete = int(input("Enter 0 or 1 [0/1]: "))

    task = model.TDL()
    task.set_task_name(task_name)
    task.set_task_desc(task_desc)
    task.set_task_due_date(task_due_date)
    task.set_isComplete(task_isComplete)

    tdl_data.add_task(task)


def view_all_tasks():
    task_list = tdl_data.view_tasks()
    print(f"\nCurrent number of tasks: {len(task_list)}\n")
    print("-----------------------------------------------------------------------------------------------------------------------------")
    for task in task_list:
        print(f"Task-ID: {task.get_task_id()}")
        print(f"Task-Name: {task.get_task_name()}")
        print(f"Task-Description: {task.get_task_desc()}")
        print(f"Task-Due_Date: {task.get_task_due_date()}")
        print(f"Task-isComplete: {task.get_isComplete()}")
        print("-----------------------------------------------------------------------------------------------------------------------------")


def mark_task_complete():
    view_all_tasks()
    task_id = int(input("\nEnter Task ID to Mark as complete: "))
    result = tdl_data.mark_task_complete(task_id)
    if result is None:
        print(f"\nNo Task Found With Task-ID {task_id}!")
    else:
        if not result: #result == false
            print("\n -- Task Already Marked As Complete! --")
        else:
            print(f"\nTask With ID {task_id} Marked As Complete Successfully!")


def delete_task():
    view_all_tasks()
    task_id = int(input("Enter Task ID to delete: "))
    result = tdl_data.delete_task(task_id)
    if result:
        print("\nTask Deleted Successfully!!!")

if __name__ == "__main__":
    menu()
    try:
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            add_task()

        elif choice == 2:
            view_all_tasks()

        elif choice == 3:
            mark_task_complete()

        elif choice == 4:
            delete_task()

        elif choice == 5:
            print("\nExiting!!")
            sys.exit(0)
        else:
            print("\nInvalid Choice!")
    except ValueError:
        print("\nPlease Enter a valid Input!")
    except Exception as err:
        print(f"Something unexpected has occurred: {err}")
