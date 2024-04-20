import threading

from OrderQueue import OrderQueue
from Bot import Bot


class BotManager:
    def __init__(self, callback=None):
        self.bots = []
        self.orders = OrderQueue()
        self.callback = callback
        self.next_bot_id = 0

    def add_bot(self):
        bot = Bot(bot_id=self.next_bot_id, callback=self.notify_status)
        self.bots.append(bot)
        self.next_bot_id += 1
        self.assign_orders()
        self.notify_status(f"Bot {bot.bot_id} added and is idle")

    def remove_bot(self):
        if self.bots:
            bot = self.bots.pop()
            self.notify_status(f"Bot {bot.bot_id} removed")
            if not bot.idle:
                # Return the current order to the queue if the bot was processing it
                self.orders.orders.appendleft(bot.current_order)

    def notify_status(self, message):
        print(message)
        self.assign_orders()  # Re-assign orders as needed

    def assign_orders(self):
        for bot in self.bots:
            if bot.idle and len(self.orders.orders) > 0:
                bot.idle = False
                order = self.orders.next_order()
                threading.Thread(target=bot.process_order, args=(order,)).start()

