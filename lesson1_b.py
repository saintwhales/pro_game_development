class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old.")


std1 = Student("Nameerah", 25)
std1.introduce()
std2 = Student("daniel", 13)
std2.introduce()
