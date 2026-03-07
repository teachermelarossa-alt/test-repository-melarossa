class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def introduce_person(self):
        return f"Человек{self.name},возраст{self.age},пол{self.sex}"