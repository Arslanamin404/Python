## ORM (Object-Relational Mapping):

- ORM is a programming technique that facilitates the interaction between object-oriented code and relational databases. It allows developers to work with database data using object-oriented models, where database tables are represented as classes and rows as objects.

## DAO (Data Access Object):

- DAO is a design pattern used to separate the data access logic from the rest of the application. It typically involves creating a set of classes or methods that encapsulate the interaction with a database or external data source. The DAO pattern provides a clean and structured way to perform database operations like insert, update, delete, and query. It abstracts the underlying database details, making it easier to switch databases or update the data access code without affecting the rest of the application.

## Files

1. Model.py:

   - This file typically contains the data models or classes that represent the structure of the data in your application. These classes may define attributes, methods, and relationships between different data entities. For example, if your application deals with employees, this file might include an Employee class with attributes like name, ID, and department. This file contains setter and getter methods.

2. Connection.py:

   - The Connection.py file usually contains code related to database connections or network connections. It can include functions or classes for establishing, managing, and closing connections to a database or other external services. For instance, if your application interacts with a database, you might find code here for connecting to that database.

3. EmployeeDAO.py:

   - EmployeeDAO (Data Access Object) typically contains code for database operations related to the Employee model. This file may include functions or methods for creating, reading, updating, and deleting employee records in the database. It acts as an intermediary between the application and the database, handling the data access logic.

4. Main.py:
   - Main.py often serves as the entry point of your application. It may contain the code that ties all the components together, such as initializing the database connection, creating instances of the EmployeeDAO class, and executing the main application logic. This is where you might run your application and perform tasks like handling user input, displaying information, and orchestrating the flow of the program.
