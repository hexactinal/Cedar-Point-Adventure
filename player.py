import time
import random


class Player:
    def __init__(self, cheat=None):
        if cheat is None:
            self.cheat = False
        else:
            self.cheat = True

        self.health = 100
        self.magic = 20
        self.wallet = 100
        self.inventory = []

    def spend_money(self, amount):
        self.wallet = self.wallet - amount
        print(f"You pay the ${amount}, and now you have ${self.wallet}.")
        time.sleep(2)

    def attack(self, enemy_a):
        damage_amount = random.randint(1, 10)
        print(f"You attack {enemy_a.name} for {damage_amount} HP.")
        time.sleep(0.5)
        return damage_amount

    def fire_attack(self, enemy_a):
        if self.magic < 10:
            print("You do not have enough magic to do a Fireball attack.")
            time.sleep(0.5)
            print("[It costs 10 PP]")
            # I'm returning 0 here to indicate that the player
            # did not have enough magic. Don't forget to do the check
            # in the main file as well.
            return 0
        damage_amount = random.randint(15, 30)
        self.magic = self.magic - 10
        print(f"You shoot flames at {enemy_a.name} for {damage_amount} HP.")
        time.sleep(0.5)
        print(f"Your magic is now {self.magic} PP.")
        time.sleep(0.5)
        return damage_amount

    def take_damage(self, damage_amount):
        self.health = self.health - damage_amount
        if self.health >= 0:
            print(f"Your health: {self.health} HP.")
        else:
            print("Your health: 0 HP.")
        time.sleep(0.5)

    def heal_self(self, heal_amount=None):
        if heal_amount is None:
            heal_amount = 20
        if self.magic < 5:
            print("You do not have enough magic to heal yourself.")
            time.sleep(0.5)
            print("[It costs 5 PP]")
            return
        if self.health + heal_amount < 100:
            print(f"Healed {heal_amount} HP.")
            self.health = self.health + heal_amount
        else:
            print(f"Healed {100 - self.health} HP.")
            self.health = 100
        self.magic = self.magic - 5
        print(f"Your health is now {self.health} HP.")
        time.sleep(0.5)
        print(f"Your magic is now {self.magic} PP.")
        time.sleep(0.5)

    def look_at_items(self):
        if len(self.inventory) == 0:
            print("No items in your inventory!")
            return []
        print(f"Your items: {self.inventory}")
        return self.inventory

    def death_message(self, enemy_name=None):
        if enemy_name is None:
            print("Generic Enemy killed you.")
        else:
            print(f"{enemy_name} killed you.")
        time.sleep(0.5)
