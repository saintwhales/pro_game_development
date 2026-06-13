# Hybrid Inheritance

# GrandParent Class


class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name: {self.name}")


# Parent Class 1
class Employee(Person):
    def __init__(self, name, emp_id):
        Person.__init__(self, name)
        self.emp_id = emp_id

    def show_employee(self):
        print(f"Employee ID: {self.emp_id}")


# Parent Class 2
class Trainer(Person):
    def __init__(self, name, subject):
        Person.__init__(self, name)
        self.subject = subject

    def show_subject(self):
        print(f"Subject: {self.subject}")


# Child Class
class TechTrainer(Employee, Trainer):
    def __init__(self, name, emp_id, subject):
        Employee.__init__(self, name, emp_id)
        Trainer.__init__(self, name, subject)

    def display_details(self):
        self.show_name()
        self.show_employee()
        self.show_subject()


trainer = TechTrainer("Daniel Brown", "Tr501", "Cloud Computing")
trainer.display_details()
