class Car:
    def __init__(self, name, model, age):
        self.name = name
        self.model = model
        self.age = age
    def introduce_car(self):
        print(f"Человек {self.name},  возраст {self.model},пол {self.age} ")
class Exercise:
    def __init__(self, name, calories_per_min ):
        self.name = name
        self.calories_per_min = calories_per_min
    def get_info(self):
        return (f"Название: {self.name}, Цена: {self.calories_per_min}")


        