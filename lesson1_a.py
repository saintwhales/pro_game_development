class Student:
    def __init__(self, name, age, scclass, teacher):
        self.name = name
        self.age = age
        self.scclass = scclass
        self.teacher = teacher

    def change_details(self):
        print("Please enter your age: ")
        self.age = int(input())
        print("Please enter the name of the student: ")
        self.name = input()

    def show_details(self):
        print("The details of student are: ")
        print(self.name)
        print(self.age)
        print(self.scclass)
        print(self.teacher)


Daniel = Student("Daniel", 13, 9, "Nameerah Kazi")
Daniel.change_details()
Daniel.show_details()
Alex = Student("Alex", 17, 17, "Sayani")
Alex.change_details()
Alex.show_details()
