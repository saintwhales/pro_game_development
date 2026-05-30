class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def show_details(self):
        print("The details of the dog are: ")
        print(self.name)
        print(self.breed)


Max = Dog("Max", "German Shepherd")
Max.show_details()
Max.bark()
