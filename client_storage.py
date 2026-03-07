import json
from client import clients, Client

'''class Client:
    def __init__(self, name, is_loyal):
        self.name = name
        self.is_loyal = is_loyal
    
    def to_dict(self):
        return {"name":self.name, "is.loyal":self.is_loyal}'''




class ClientStorage:
    def __init__(self, clients):
        self.clients  = clients


    def add_client(self, client : Client):
        self.clients.append(client)
        return self.clients



    # вернуть всех клиентов
    def get_all(self):
        return self.clients



    # вернуть только лояльных клиентов
    def get_loyal_clients(self):
        return [c for c in self.clients if c.is_loyal]



    # сохранить всех клиентов в json -использовать client.to_dict для каждого
    def save_to_json(self, filename="clients.json"):
        with open(filename, 'w', encoding='utf-8') as f:
            for client in self.clients:
                f.write(f"{client.to_dict()} \n")

c = ClientStorage(clients)
#print(c.get_all())
c.add_client(Client('афвфыв', '4242421', 'fsfsdfs@dfs.com', 0, 0, True))
print(c.get_loyal_clients())

c.save_to_json()