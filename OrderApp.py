import threading
from cmd import Cmd

from BotManager import BotManager
from Order import Order


class OrderApp(Cmd):
    prompt = "(McDonalds) "

    def __init__(self):
        super().__init__()
        self.bot_manager = BotManager(callback=self.order_completed)

    def do_new_normal_order(self, arg):
        order = Order("NORMAL")
        self.bot_manager.orders.add_order(order)
        print(f"Added: {order}")
        self.bot_manager.assign_orders()

    def do_new_vip_order(self, arg):
        order = Order("VIP")
        self.bot_manager.orders.add_order(order)
        print(f"Added: {order}")
        self.bot_manager.assign_orders()

    def do_add_bot(self, arg):
        self.bot_manager.add_bot()
        print("Bot.py added")

    def do_remove_bot(self, arg):
        self.bot_manager.remove_bot()
        print("Bot.py removed")

    def order_completed(self, order):
        print(f"Real-time update: Order {order.id} has been completed!")


if __name__ == "__main__":
    app = OrderApp()
    app.cmdloop()
