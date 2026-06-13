# Miltiple Inheritance (2 parents - - 1 child)

# Parent 1


class Salary:
    def __init__(self, salary):
        self.salary = salary

    def show_salary(self):
        print(f"Salary: {self.salary}")


# Parent 2


class Benefits:
    def __init__(self, insurance):
        self.insurance = insurance

    def show_benefits(self):
        print(f"Insurance Plan: {self.insurance}")


# Child Class


class Manager(Salary, Benefits):
    def __init__(self, name, salary, insurance):
        Salary.__init__(self, salary)
        Benefits.__init__(self, insurance)
        self.name = name

    def display_details(self):
        print(f"Manager Name: {self.name}")
        self.show_salary()
        self.show_benefits()


manager = Manager("John Smith", 85000, "Premium Health Cover")
manager.display_details()
