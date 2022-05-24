import time


class Player:
    def __init__(self, cheat=None):
        if cheat is None:
            self.cheat = False
        else:
            self.cheat = True

        self.wallet = 100

    def spend_money(self, amount):
        self.wallet = self.wallet - amount
        print(f"You pay the ${amount}, and now you have ${self.wallet}.")
        time.sleep(2)
