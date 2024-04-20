import threading
import time


class Bot:
    def __init__(self, bot_id, callback=None):
        self.bot_id = bot_id
        self.idle = True
        self.callback = callback

    def process_order(self, order):
        self.update_status(f"Bot {self.bot_id} starts processing Order {order.id}")
        time.sleep(10)  # Simulate processing time
        order.status = "COMPLETE"
        self.update_status(f"Bot {self.bot_id} finished processing Order {order.id}")
        self.idle = True
        self.update_status(f"Bot {self.bot_id} is now idle")

    def update_status(self, message):
        if self.callback:
            self.callback(message)
