class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def get_status(self):
        if self.grade > 8:
            return "отлично"
        else:
            return "удовлетворительно"


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
    def teach(self):
        print(f"Учитель {self.teacher.name} преподает {self.teacher.subject}")

