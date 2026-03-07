class Order:
    STATUSES = ['новый','в работе','готов','выполнен']
    def __init__(self, order_id, bouquet, price):
        self.order_id = order_id
        self.bouquet = bouquet
        self.price = price
        self.status = 'новый'
        self.completed_at = None
    def change_status(self,new_status):
        if new_status in self.STATUSES:
            self.status = new_status
            return True
        else:
            return False
    def is_completed(self):
        return self.status == 'выполнен'
    def to_dict(self):
        return {
            'order_id': self.order_id,
            'bouquet' : self.bouquet,
            'price' : self.price,
            'status' : self.status,
            'completed_at' : self.completed_at
        }
if __name__ == "__main__":
    order = Order('1234', 'розы', '50')
    print(order.to_dict())
    order.change_status('в работе')
    print(order.to_dict())
    print(f"Завершен:{order.is_completed()}")

    

        