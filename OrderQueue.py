from collections import deque


class OrderQueue:
    def __init__(self):
        self.orders = deque()

    def add_order(self, order):
        if order.order_type == "VIP":
            position = 0
            for o in self.orders:
                if o.order_type == "NORMAL":
                    break
                position += 1
            self.orders.insert(position, order)
        else:
            self.orders.append(order)

    def next_order(self):
        if self.orders:
            return self.orders.popleft()
        return None
