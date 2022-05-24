import time
import random


class Enemy:
    def appears(self):
        print(f"You come across {self.name} with {self.hp} HP.")
        time.sleep(0.5)

    def __init__(self, name=None, hp=None):
        if name is None:
            self.name = "Generic Enemy"
        else:
            self.name = name
        if hp is None:
            self.hp = 20
        else:
            self.hp = hp
        self.appears()

    def attack(self):
        damage_amount = random.randint(1, 10)
        print(f"{self.name} attacks Player for {damage_amount} HP.")
        time.sleep(0.5)
        return damage_amount

    def take_damage(self, damage_amount):
        self.hp = self.hp - damage_amount
        if self.hp >= 0:
            print(f"{self.name} health: {self.hp} HP.")
        else:
            print(f"{self.name} health: 0 HP.")
