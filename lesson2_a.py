class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        if salary > 0:
            self.salary = salary
        else:
            print("Invalid salary")

    def add_bonus(self, bonus):
        if bonus > 0:
            self.salary += bonus
        else:
            print("Invalid bonus")

    def display(self):
        print("Employee: ", self.name)
        print("salary: ", self.salary)
        print("--------------------")


e1 = Employee("John", 30000)
e1.display()

e1.add_bonus(5000)
print("After bonus: ", e1.get_salary())

e1.set_salary(-1000)
e1.set_salary(40000)
e1.display()

e2 = Employee("Alex", 50000)
e2.display()

e2.add_bonus(10000)
print("After bonus: ", e2.get_salary())

e2.set_salary(80000)
e2.display()
