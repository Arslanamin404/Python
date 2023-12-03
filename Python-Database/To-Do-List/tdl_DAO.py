import connection
import model


class TDL_DAO:
    def __init__(self):
        try:
            self.__con = connection.MyDatabase.get_connection()
            print("\nConnected To MySQL DB\n")
            self.__cursor = self.__con.cursor()
        except Exception as err:
            print(f"An Error Has Occurred :{err}")

    def add_task(self, task):
        try:
            query = "INSERT INTO tasks (name, description, due_date, is_complete) VALUES (%s, %s, %s,%s)"
            data = (task.get_task_name(), task.get_task_desc(),
                    task.get_task_due_date(), task.get_isComplete())
            self.__cursor.execute(query, data)
            self.__con.commit()
            print("\nTask Inserted Successfully!")
        except Exception as err:
            print(f"\nAn Error Has Occurred: {str(err)}")

    def view_tasks(self):
        tasks = []
        try:
            query = "SELECT * FROM tasks"
            self.__cursor.execute(query)
            result = self.__cursor.fetchall()
            for row in result:
                task1 = model.TDL()
                task1.set_task_id(row[0])
                task1.set_task_name(row[1])
                task1.set_task_desc(row[2])
                task1.set_task_due_date(row[3])
                task1.set_isComplete(row[4])
                tasks.append(task1)
            return tasks
        except Exception as err:
            print(f"\nAn Error Has Occurred: {str(err)}")

    def mark_task_complete(self, task_id):
        try:
            query = "SELECT * FROM tasks WHERE id = %s"
            self.__cursor.execute(query, (task_id,))
            result = self.__cursor.fetchone()
            if result is None:
                return None
            elif result[4] == 1:
                return False
            else:
                task = model.TDL()
                task.set_task_id(result[0])
                task.set_isComplete(1)  # Mark as complete
                update_query = "UPDATE tasks SET is_complete = 1 WHERE id = %s"
                self.__cursor.execute(update_query, (task.get_task_id(),))
                self.__con.commit()
                return True
        except Exception as err:
            print(f"An Error Has Occurred: {str(err)}")

    def delete_task(self, task_id):
        try:
            # First, check if the task exists
            query = "SELECT * FROM tasks WHERE id = %s"
            self.__cursor.execute(query, (task_id,))
            result = self.__cursor.fetchone()
            if result is None:
                print(f"Task with ID {task_id} not found.")
                return False

            # If the task exists, proceed to delete it
            delete_query = "DELETE FROM tasks WHERE id = %s"
            self.__cursor.execute(delete_query, (task_id,))
            self.__con.commit()
            print(f"Task with ID {task_id} has been deleted.")
            return True
        except Exception as err:
            print(f"An Error Has Occurred: {err}")
            return False  # Deletion failed due to an error

    def __del__(self):
        try:
            self.__con.close()
            print(
                "\n----------------------------\nConnection Closed!\n----------------------------\n")
        except Exception as err:
            print(f"An Error Has Occurred: {err}")
