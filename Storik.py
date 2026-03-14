class OnlineStore:
    def __init__(self,name):
        # Атрибуты класса
        self.name = name
        self.products = []
        self.orders = []
    

    # добавление товара в магазин
    def add_product(self,name,price,stock):
        product = {'name':name, 'price':price, 'stock':stock}
        self.products.append(product)


    # все товары
    def show_products(self):
        if not self.products:
            print('В магазине пусто')
        else:
            print(f"Список в '{self.name}': ")
            for products in self.products:
                print(f"{products['name']} - ${products['price']} | x{products['stock']}")
    

    # найти товар
    def find_product(self,name):
        for product in self.products:
            if product['name'] == name:
                return product
        return None
    

    # удаление товара
    def remove_product(self,name):
        product = self.find_product(name)
        if product:
            self.products.remove(product)
            print(f'Вы удалили "{name}" из списка')
        else:
            print(f'Товара "{name}" нет в списке')
    

    # завоз
    def restock_product(self,name,amount):
        product = self.find_product(name)
        if product:
            product['stock'] += amount
            print(f'Вы пополнили "{name}" на x{amount}. Теперь на складе x{product["stock"]}')
        else:
            print(f'Товара "{name}" нет в списке')

    
    # сделать заказ (добавление в orders, уменьшение в stock)
    def make_order(self,name,amount):
        product = self.find_product(name)
        if product and product['stock'] >= amount:
            product['stock'] -= amount
            price = product['price'] * amount
            order = {'product':name,
                     'amount':amount,
                     'price':price}
            self.orders.append(order)
            print(f'Добавлен заказ: {name} - ${price} | x{amount} ')
        else:
            print('Не удалось сделать заказ')


    # все заказы
    def show_orders(self):
        if not self.orders:
            print('Заказов нет')
        else:
            for order in self.orders:
                print(f"{order['product']} - ${order['price']} | x{order['amount']}")
            
    
    # сумма заказов
    def total_revenue(self):
        return sum(order['price'] for order in self.orders)
    

    # самый маст хев товар
    def most_popular_product(self):
        if not self.orders:
            return None
        sold = {}
        for order in self.orders:
            name = order['product']
            sold[name] = sold.get(name, 0) + order['amount']
        
        pop = max(sold, key=sold.get)
        return pop
    

    def __str__(self):
        return f"OnlineStore: {self.name} (Товаров: {len(self.products)}, Заказов: {len(self.orders)})"

store = OnlineStore('Xikato Scam')

store.add_product('Laptop',1200,5)
store.add_product('Mouse',25,50)
store.add_product('Keyboard',80,10)

store.show_products()

store.make_order('Laptop',1)
store.make_order('Mouse',3)

store.show_orders()

print('Revanue:', store.total_revenue())

store.restock_product('Laptop',5)

#store.remove_product('Keyboard')

store.most_popular_product()

print(store)

