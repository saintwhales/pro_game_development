# Multilevel Inheritance GP -- P -- C

# Grandparent Class


class Person:
    def __init__(self, name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")


# Parent Class


class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def display_employee(self):
        print(f"Employee ID: {self.emp_id}")


# Child Class


class TeamLead(Employee):
    def __init__(self, name, emp_id, team_size):
        super().__init__(name, emp_id)
        self.team_size = team_size

    def display_teamlead(self):
        self.display_name()
        self.display_employee()
        print(f"Team Size: {self.team_size}")


lead = TeamLead("David Wilson", "TL201", 12)
lead.display_teamlead()
