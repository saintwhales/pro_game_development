# SINGLE INHERITANCE

# Parent Class


class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def displayEmployee(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.name}")


# Child Class
class Developer(Employee):
    def __init__(self, emp_id, name, programming_language):
        super().__init__(emp_id, name)
        self.programming_language = programming_language

    def display_developer(self):
        self.displayEmployee()
        print(f"Programming Language: {self.programming_language}")


dev = Developer("E101", "John Smith", "Python")
dev.display_developer()
