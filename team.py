class Student:
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
    def get_status(self):
        if self.grade > 8:
            return "отлично"
        else:
            return "удовлетворительно"