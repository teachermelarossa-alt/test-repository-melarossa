class Car:
    def __init__(self, name, model, age):
        self.name = name
        self.model = model
        self.age = age
    def introduce_car(self):
        print(f"Человек {self.name},  возраст {self.model},пол {self.age} ")