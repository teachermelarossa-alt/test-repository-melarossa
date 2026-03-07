CafeCRM Система Лояльности Кафе
Команда 1
Стажер 1
1. Создать файл client.py с классом Client
необходимо в классе сохранить атрибуты name,phone,email - убрать пробелы по краям
также необходимо сохранить visits - кол-во посещение по умолчанию 0
total_spent = 0.0 - сколько всего потрачено

Методы:
add_purchase(self,amount) - добавить покупку
увеличить кол-во visits на 1
добавить к total_spent amount
is_loyal - если visits > 5 то True
to_dict - преобразовать информацию класса в словарь:
пример 1. {'name': 'Ivan', 'total_spent':100.0}

2. Стажер 2
Создать файл client_storage.py
атрибуты - clients - пустой список
def add_client - добавить клиента в список
def get_all - вернуть всех клиентов
def get_loyal_clients - вернуть только лояльных клиентов
def _save - сохранить всех клиентов в json -
использовать client.to_dict для каждого

3. Стажер 3
создать файл business_logic.py
создать функции:
def get_top_clients(storage: ClientStorage)-
вернуть клиентов кто больше тратит от большего к меньшеу
def total_revenue (storage: ClientStorage) - Общая выручка, сумма total_spent - всех клиентов
def average_check(storage: ClientStorage) - средний чек, если визитов нет вернуть 0.0
нужно total_revenue/общее кол-во визитов

4. Стажер 4 
создать фалй cafe_crm.py
Полный рабочий продукт
1.Добавить клиента
2. Все клиенты
3. Топ 3-клиента
4. Лояльные клиенты
5. Статистика
6. Выход

==================================================================
Команда 2
FlowerCRM
1. Стажер 1
Файл order.py
class Order:
    У класс есть статусы, общее для всех STATUSES = ['новый','в работе','готов','выполнен']
def __init__(self, order_id, bouquet, price)
    добавить тут статус 'новый'
    completed_at = None
создать метод 
def change_status(self,new_status)
Проверить что new_status в STATUSES
если все ок то отвечаем True
иначе False
def is_completed - вернуть True если status == 'выполнен'

def to_dict - перевести атрибуты класс в словарь json
{'order_id':'1234','bouquet':'розы','price':'50', 'status'='в работе', 'completed_at' = None}