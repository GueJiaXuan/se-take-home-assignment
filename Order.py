class Order:
    id_counter = 0

    def __init__(self, order_type):
        self.id = Order.id_counter
        Order.id_counter += 1
        self.order_type = order_type
        self.status = "PENDING"

    def __repr__(self):
        return f"Order(ID: {self.id}, Type: {self.order_type}, Status: {self.status})"

