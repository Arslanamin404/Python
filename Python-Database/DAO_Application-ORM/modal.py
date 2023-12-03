class Employee:
    # Setters
    def set_id(self, emp_id):
        self.__emp_id = emp_id

    def set_name(self, emp_name):
        self.__emp_name = emp_name

    def set_department(self, emp_dept):
        self.__emp_dept = emp_dept

    def set_salary(self, emp_salary):
        self.__emp_salary = emp_salary

    # Getters
    def get_id(self):
        return self.__emp_id

    def get_name(self):
        return self.__emp_name

    def get_department(self):
        return self.__emp_dept

    def get_salary(self):
        return self.__emp_salary
