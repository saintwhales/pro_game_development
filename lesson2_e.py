# Hierarchical Inheritance (multiple child classes)

# Parent Class


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print(f"Brand: {self.brand}")


# Child 1


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def display_car(self):
        self.show_brand()
        print(f"Car Model: {self.model}")


# Child 2


class Bike(Vehicle):
    def __init__(self, brand, engine_cc):
        super().__init__(brand)
        self.engine_cc = engine_cc

    def display_bike(self):
        self.show_brand()
        print(f"Engine Capacity: {self.engine_cc}")


# obj1
car = Car("BMW", "M4")
car.display_car()
print("-" * 40)

# obj2
bike = Bike("BMW S 1000 RR", "999 CC")
bike.display_bike()
