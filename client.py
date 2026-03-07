class Client:
    def __init__(self, name, phone, email, visits = 0, total_spent = 0.0, is_loyal = False):
        self.name = name
        self.phone = phone
        self.email = email
        self.visits = visits
        self.total_spent = total_spent
        self.is_loyal = is_loyal

    def __str__(self):
        return f"{self.name}, {self.phone}"

    def add_purchase(self,amount):
        self.visits +=1
        self.total_spent += amount
        if self.visits > 5 and not self.is_loyal:
            self.is_loyal = True

    def to_dict(self):
        return {"name": self.name, "vists": self.visits, "total_spent": self.total_spent}


clients = [
    Client("Ivan Ivanov", "+12345678901", "ivan1@example.com"),
    Client("Petr Petrov", "+12345678902", "petr2@example.com"),
    Client("Anna Smirnova", "+12345678903", "anna3@example.com"),
    Client("Sergey Kuznetsov", "+12345678904", "sergey4@example.com"),
    Client("Olga Popova", "+12345678905", "olga5@example.com"),
    Client("Dmitry Sokolov", "+12345678906", "dmitry6@example.com"),
    Client("Elena Lebedeva", "+12345678907", "elena7@example.com"),
    Client("Alexey Kozlov", "+12345678908", "alex8@example.com"),
    Client("Natalia Novikova", "+12345678909", "nat9@example.com"),
    Client("Andrey Morozov", "+12345678910", "andrey10@example.com"),
    Client("Maria Volkova", "+12345678911", "maria11@example.com"),
    Client("Nikolay Pavlov", "+12345678912", "nik12@example.com"),
    Client("Tatiana Semenova", "+12345678913", "tanya13@example.com"),
    Client("Vladimir Golubev", "+12345678914", "vlad14@example.com"),
    Client("Irina Vinogradova", "+12345678915", "irina15@example.com"),
    Client("Maxim Bogdanov", "+12345678916", "max16@example.com"),
    Client("Yulia Vorobyova", "+12345678917", "yulia17@example.com"),
    Client("Denis Fedorov", "+12345678918", "denis18@example.com"),
    Client("Svetlana Mikhailova", "+12345678919", "sveta19@example.com"),
    Client("Roman Belyaev", "+12345678920", "roman20@example.com"),
]