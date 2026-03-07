class Client:
    def __init__(self, name, phone, email, visits = 0, total_spent = 0.0, is_loyal = False):
        
        def add_purchase(self,amount):
            self.visits +=1
            self.total_spent += amount
            self.visits += 1
            self.is_loyal = True if visits > 5 else False

        def to_dict(self):
            

clients = [
    Clients("Ivan Ivanov", "+12345678901", "ivan1@example.com"),
    Clients("Petr Petrov", "+12345678902", "petr2@example.com"),
    Clients("Anna Smirnova", "+12345678903", "anna3@example.com"),
    Clients("Sergey Kuznetsov", "+12345678904", "sergey4@example.com"),
    Clients("Olga Popova", "+12345678905", "olga5@example.com"),
    Clients("Dmitry Sokolov", "+12345678906", "dmitry6@example.com"),
    Clients("Elena Lebedeva", "+12345678907", "elena7@example.com"),
    Clients("Alexey Kozlov", "+12345678908", "alex8@example.com"),
    Clients("Natalia Novikova", "+12345678909", "nat9@example.com"),
    Clients("Andrey Morozov", "+12345678910", "andrey10@example.com"),
    Clients("Maria Volkova", "+12345678911", "maria11@example.com"),
    Clients("Nikolay Pavlov", "+12345678912", "nik12@example.com"),
    Clients("Tatiana Semenova", "+12345678913", "tanya13@example.com"),
    Clients("Vladimir Golubev", "+12345678914", "vlad14@example.com"),
    Clients("Irina Vinogradova", "+12345678915", "irina15@example.com"),
    Clients("Maxim Bogdanov", "+12345678916", "max16@example.com"),
    Clients("Yulia Vorobyova", "+12345678917", "yulia17@example.com"),
    Clients("Denis Fedorov", "+12345678918", "denis18@example.com"),
    Clients("Svetlana Mikhailova", "+12345678919", "sveta19@example.com"),
    Clients("Roman Belyaev", "+12345678920", "roman20@example.com"),
]
