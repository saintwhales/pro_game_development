class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def show_details(self):
        print("\nThe details of the animal are: ")
        print("Animal name: " + self.name)
        print("Animal sound: " + self.sound)


dog = Animal("Dog", "Woof Woof!")
dog.show_details()

cat = Animal("Cat", "Meow Meow!")
cat.show_details()

cow = Animal("Cow", "Moo Moo!")
cow.show_details()

lion = Animal("Lion", "Roar!")
lion.show_details()

duck = Animal("Duck", "Quack Quack!")
duck.show_details()
