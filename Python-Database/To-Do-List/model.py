class TDL:
    # Setters
    def set_task_id(self, task_id):
        self.task_id = task_id

    def set_task_name(self, task_name):
        self.task_name = task_name

    def set_task_desc(self, task_desc):
        self.task_desc = task_desc

    def set_task_due_date(self, due_date):
        self.task_due_date = due_date

    def set_isComplete(self, isComplete):
        self.isComplete = isComplete

    # getters
    def get_task_id(self):
        return self.task_id

    def get_task_name(self):
        return self.task_name

    def get_task_desc(self):
        return self.task_desc

    def get_task_due_date(self):
        return self.task_due_date

    def get_isComplete(self):
        return self.isComplete
