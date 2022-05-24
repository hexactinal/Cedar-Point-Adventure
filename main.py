#!/usr/bin/python3

import time
import sys
from player import Player

player_a = Player()


def slow_char_display(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    # This adds an extra newline so that you don't have to add a '\n'
    # at the end of each string.
    print()


def get_usr_input(valid_options):
    print('What do you want to do?')
    usr_in = input("> ")
    while usr_in.lower() not in valid_options:
        print(f"{usr_in} is not a valid option! Please try again.")
        print(f"Options: {valid_options}")
        print('What do you want to do?')
        usr_in = input("> ")

    return usr_in


def exit_msg():
    # print("***Thanks for playing!!!***")
    with open('thanks_msg.txt', 'r') as f:
        for line in f:
            print(line)
            time.sleep(0.08)


def main():

    # Check if "--cheat" is passed to the game.
    # If so, then turn cheats on.
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "--cheat":
                player_a.cheat = True

    if player_a.cheat:
        print(
            "[WARNING] You have cheats enabled. Debug messages are on and achievements are disabled."
        )

    print("Welcome to the Cedar Point Adventure!")
    print("You start on the peninsula,")
    print("and you can see the coaster skyline on the horizon.")
    valid_options = ["drive closer", "turn back"]
    usr_in = get_usr_input(valid_options)
    if usr_in != "Turn back":
        print("It's kooky...")
        time.sleep(2)
        print("It's spooky...")
        time.sleep(2)
        print("Time for some crazy fun!")
        time.sleep(2)
        print("You come up to the toll booth.")
        time.sleep(2)
        valid_options = ["pay toll", "beat up toll worker"]
        usr_in = get_usr_input(valid_options)
        if usr_in.lower() == "beat up toll worker":
            print("You attempt to beat up the toll worker,")
            time.sleep(2)
            print("but you did not see that they had a gun.")
            time.sleep(2)
            print("[GAME OVER]")
            time.sleep(2)
        elif usr_in.lower() == 'pay toll':
            print("You pay the fee to enter the park.")
            time.sleep(2)
            print("It's a busy weekend this time.")
            time.sleep(2)
            print('In fact, Cedar Point is doing its "HalloWeekends" event right now.')
            time.sleep(2)
            s1 = 'You think to yourself: "Wow, it looks so cool up close!"'
            slow_char_display(s1)
            print("The area is crowded with people,")
            time.sleep(2)
            print("and you can hear screams in the distance.")
            time.sleep(2)
            print("There are many options to get into the park.")
            time.sleep(2)
            valid_options = [
                "pay for ticket",
                "sneak past entrance",
                "walk along beach",
            ]
            usr_in = get_usr_input(valid_options)
            if usr_in.lower() == "pay for ticket":
                pay_ticket()
            elif usr_in.lower() == "sneak past entrance":
                sneak_past_entrance()
            elif usr_in.lower() == "walk along beach":
                walk_along_beach()

    else:
        leave_park()

    exit_msg()


def pay_ticket():
    s1 = '[Michael] "Welcome to Cedar Point! Tickets are $45 per person."'
    slow_char_display(s1)
    player_a.spend_money(45)
    s2 = '[Michael] "Have a great day!"'
    slow_char_display(s2)
    print("The park lies in front of you.")
    time.sleep(2)
    print("There are a few options for where to go.")
    time.sleep(2)
    valid_options = ["raptor", "zombie high school", "leave park"]
    usr_in = get_usr_input(valid_options)
    if usr_in.lower() == "raptor":
        raptor()
    elif usr_in.lower() == "zombie high school":
        zombie_high()
    elif usr_in.lower() == "leave park":
        leave_park()


def raptor():
    pass


def zombie_high():
    pass


def leave_park():
    print("But the stress of going to HalloWeekends overwhelmed you.")
    time.sleep(2)
    print("You leave to see Cedar Point another day.")
    time.sleep(2)


def sneak_past_entrance():
    pass


def walk_along_beach():
    pass


if __name__ == "__main__":
    main()
