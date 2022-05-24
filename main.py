#!/usr/bin/python3

import time
import sys
import random
import webbrowser
from player import Player
from enemy import Enemy

player_a = Player()


def slow_char_display(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.08)
    # This adds an extra newline so that you don't have to add a '\n'
    # at the end of each string.
    print()


def get_usr_input(valid_options):
    # print('What do you want to do?')
    usr_in = input("?> ")
    for option in valid_options:
        if len(usr_in) == 0:
            return option
        if usr_in[0] == option[0]:
            return option
    while usr_in.lower() not in valid_options:
        if usr_in.lower() != "help" and usr_in != "H":
            print(f"{usr_in} is not a valid option! Please try again.")
        print(f"Options: {valid_options}")
        # print('What do you want to do?')
        usr_in = input("?> ")
        for option in valid_options:
            if len(usr_in) == 0:
                return option
            if usr_in[0] == option[0]:
                return option

    return usr_in


def battle_enemy(enemy_a):
    while enemy_a.hp > 0:
        # This is for the "run" check later in the function.
        run_success = 0
        if player_a.health <= 0:
            player_a.death_message(enemy_a.name)
            exit_msg()
        valid_options = ["attack", "magic", "item", "run"]
        usr_in = get_usr_input(valid_options)
        if usr_in.lower() == "attack":
            player_damage_amount = player_a.attack(enemy_a)
            enemy_a.take_damage(player_damage_amount)
        elif usr_in.lower() == "magic":
            if player_a.magic > 5:
                valid_options = ["lifeup", "fireball"]
                usr_in = get_usr_input(valid_options)
                if usr_in.lower() == "lifeup":
                    if player_a.health < 100:
                        player_a.heal_self()
                    else:
                        print("Your health is already at 100 HP,")
                        time.sleep(1)
                        print("so continuing with the fight...")
                elif usr_in.lower() == "fireball":
                    player_damage_amount = player_a.fire_attack(enemy_a)
                    if player_damage_amount == 0:
                        print("[Not flaming enemy since you have")
                        print("less than 10 PP]")
                        time.sleep(0.5)
                    else:
                        enemy_a.take_damage(player_damage_amount)

            else:
                print("Not enough magic to do either spell,")
                time.sleep(1)
                print("so continuing with the fight...")
                time.sleep(1)
        elif usr_in.lower() == "item":
            items = player_a.look_at_items()
            if len(items) == 0:
                print("Since you do not have any items,")
                time.sleep(1)
                print("fight is continuing...")
                time.sleep(1)
            else:
                for item in items:
                    # TODO: finish all of the options for the items.
                    # (like "use potion", etc.)
                    print(item)
        elif usr_in.lower() == "run":
            run_success = random.randint(1, 3)
            if run_success == 2:
                print("Successfully ran away!")
                time.sleep(1)
                # Since the condition to exit the loop is the enemy's health,
                # I can just set the health to 0 to "win" the fight.
                enemy_a.hp = 0
            else:
                print("Could not escape, so fight is continuing...")
                time.sleep(1)

        if run_success != 2:
            damage_amount = enemy_a.attack()
            player_a.take_damage(damage_amount)

    # If it got to this point, then the enemy health is
    # less than or equal to zero, so print the win message.
    win_msg()


def win_msg():
    # This does not exit out of the game because
    # it is used for win messages at the end of battles.
    # If the player happens to "win" the game,
    # (whatever I decide that means)
    # then this should also be printed before the exit_msg.
    with open("win_msg.txt", "r") as f:
        for line in f:
            print(line)
            time.sleep(0.08)


def exit_msg():
    # print("***Thanks for playing!!!***")
    with open("thanks_msg.txt", "r") as f:
        for line in f:
            print(line)
            time.sleep(0.08)

    exit()


def main():

    # Check if "--cheat" or '-C' is passed to the game.
    # If so, then turn cheats on.
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == "--cheat" or sys.argv[i] == "-C":
                player_a.cheat = True

    if player_a.cheat:
        print(
            "[WARNING] You have cheats enabled. Debug messages are on and achievements are disabled."
        )

        print("Go to which point in the story?")
        valid_options = [
            "raptor",
            "zombie high school",
            "sneak past guard",
            "walk along beach",
        ]
        usr_in = get_usr_input(valid_options)
        if usr_in.lower() == "raptor":
            raptor()
        elif usr_in.lower() == "zombie high school":
            zombie_high()
        elif usr_in.lower() == "sneak past guard":
            sneak_past_guard()
        elif usr_in.lower() == "walk along beach":
            walk_along_beach()
        exit_msg()

    print("Welcome to the Cedar Point Adventure!")
    print("You start on the peninsula,")
    print("and you can see the coaster skyline on the horizon.")
    print('"H" for help, or type the first letter of the option that you want.')
    valid_options = ["drive closer", "turn back"]
    usr_in = get_usr_input(valid_options)
    if usr_in.lower() != "turn back":
        print("It's kooky...")
        time.sleep(1)
        print("It's spooky...")
        time.sleep(1)
        print("Time for some crazy fun!")
        time.sleep(1)
        print("You come up to the toll booth.")
        time.sleep(1)
        valid_options = ["pay toll", "beat up toll worker"]
        usr_in = get_usr_input(valid_options)
        if usr_in.lower() == "beat up toll worker":
            print("You attempt to beat up the toll worker,")
            time.sleep(1)
            print("but you did not see that they had a gun.")
            time.sleep(1)
            print("[GAME OVER]")
            time.sleep(1)
        elif usr_in.lower() == "pay toll":
            print("You pay the fee to enter the parking lot.")
            time.sleep(1)
            print("It's a busy weekend this time.")
            time.sleep(1)
            print('In fact, Cedar Point is doing its "HalloWeekends" event right now.')
            time.sleep(1)
            s1 = 'You think to yourself: "Wow, it looks so cool up close!"'
            slow_char_display(s1)
            print("The area is crowded with people,")
            time.sleep(1)
            print("and you can hear screams in the distance.")
            time.sleep(1)
            print("There are many options to get into the park.")
            time.sleep(1)
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
    time.sleep(1)
    print("There are a few options for where to go.")
    time.sleep(1)
    valid_options = ["raptor", "zombie high school", "leave park"]
    usr_in = get_usr_input(valid_options)
    if usr_in.lower() == "raptor":
        raptor()
    elif usr_in.lower() == "zombie high school":
        zombie_high()
    elif usr_in.lower() == "leave park":
        leave_park()


def raptor():
    print("As you walk up to Raptor's entrance,")
    time.sleep(1)
    print("you hear the train roar down the first hill.")
    time.sleep(1)
    valid_options = ["get in line", "chicken out"]
    usr_in = get_usr_input(valid_options)
    if usr_in.lower() == "get in line":
        raptor_line()
    elif usr_in.lower() == "chicken out":
        chicken_out("Raptor")


def raptor_line():
    print("You get in line for Raptor.")
    time.sleep(1)
    print("You come across a rowdy guest.")
    time.sleep(1)
    s1 = '[Rowdy Guest] "Hey man, I was right here in line!"'
    slow_char_display(s1)
    guest_a = Enemy("Rowdy Guest", 40)
    battle_enemy(guest_a)
    # TODO: finish this path
    print("Congrats on finishing the fight!")
    time.sleep(1)
    print("Finally, after beating the guest in a fist fight,")
    time.sleep(1)
    print("you go up and ride Raptor.")
    print("Do you have an internet connection?")
    print("(if so, then you can watch the Raptor video.)")
    valid_options = ["yes", "no"]
    usr_in = get_usr_input(valid_options)
    if usr_in.lower() == "yes":
        print("Don't forget to come back to the game when the video is done!")
        time.sleep(2)
        raptor_link = "https://www.youtube.com/watch?v=Tb2H-8CQuyY"
        webbrowser.open(raptor_link)
        input("Press any key to continue...")
    else:
        print("Alright, well sorry for that. Have fun next time you go!")


def chicken_out(ride_name):
    print(f"But the stress of riding {ride_name} was too much for you.")
    time.sleep(1)
    print("Your face turns red from embarrassment as")
    time.sleep(1)
    print("everyone around you starts laughing at you")
    time.sleep(1)
    print(f"for not riding {ride_name}.")
    time.sleep(1)
    print("You pass out on the ground.")
    time.sleep(1)
    print("[GAME OVER]")
    time.sleep(1)
    exit_msg()


def zombie_high():
    print("You come across a teen zombie.")
    time.sleep(1)
    s1 = '[Zombie] "Blaarrgh!"'
    slow_char_display(s1)
    zombie_a = Enemy("Zombie", 50)
    battle_enemy(zombie_a)
    # TODO: finish this path


def leave_park():
    print("But the stress of going to HalloWeekends overwhelmed you.")
    time.sleep(1)
    print("You leave to see Cedar Point another day.")
    time.sleep(1)


def print_grid(grid):
    for row in grid:
        for col in row:
            print(col, end=" ")
        print()


def sneak_past_entrance():
    grid = [
        ["[", "d", " ", " ", " ", " ", " ", " ", " ", " ", "]"],
        ["[", "_", "_", "_", " ", " ", " ", " ", " ", " ", "]"],
        ["[", "_", "_", "_", "_", "_", " ", " ", " ", " ", "]"],
        ["[", "_", "_", "_", "_", "_", "_", "_", " ", " ", "]"],
        ["[", "_", "_", "_", "_", "_", "_", "_", "_", "e", "]"],
    ]
    starting_location = random.randint(1, 7)
    # print(f'start location: {starting_location}')
    start_has_been_found = False
    door_location = 1
    enemy_row = 4
    enemy_col = 9
    row_start = 0
    col_start = 0
    row_count = 0
    for row in grid:
        col_count = 0
        for col in row:
            if col == "_":
                if col_count == starting_location and not start_has_been_found:
                    row_start = row_count
                    col_start = col_count
                    start_has_been_found = True

            col_count = col_count + 1
        row_count = row_count + 1

    grid[row_start][col_start] = "p"

    # NEW GRID
    print()
    player_row = row_start
    player_col = col_start
    if player_row == door_location:
        grid[player_row][player_col] = "_"
        player_row = player_row + 2
        grid[player_row][player_col] = "p"
    if player_col == door_location:
        grid[player_row][player_col] = "_"
        player_col = player_col + 2
        grid[player_row][player_col] = "p"
    print_grid(grid)
    print()
    print("--- KEY ---")
    print("p : player")
    print("e : enemy")
    print("d : door")
    while True:
        if player_row == door_location and player_col == door_location:
            break
        if player_row == enemy_row and player_col == enemy_col:
            print("Whoops, you ran into the enemy!")
            time.sleep(1)
            print("[GAME OVER]")
            time.sleep(1)
            exit_msg()
        valid_options = ["north", "east", "south", "west"]
        usr_in = get_usr_input(valid_options)
        if usr_in.lower() == "north":
            if grid[player_row - 1][player_col] != " ":
                grid[player_row][player_col] = "_"
                player_row = player_row - 1
                grid[player_row][player_col] = "p"

        elif usr_in.lower() == "east":
            if (
                grid[player_row][player_col + 1] != "]"
                and grid[player_row][player_col + 1] != " "
            ):
                grid[player_row][player_col] = "_"
                player_col = player_col + 1
                grid[player_row][player_col] = "p"

        elif usr_in.lower() == "west":
            if grid[player_row][player_col - 1] != "[":
                grid[player_row][player_col] = "_"
                player_col = player_col - 1
                grid[player_row][player_col] = "p"

        elif usr_in.lower() == "south":
            if player_row + 1 < 5:
                grid[player_row][player_col] = "_"
                player_row = player_row + 1
                grid[player_row][player_col] = "p"

        print(f"player row: {player_row}")
        print(f"player col: {player_col}")
        print_grid(grid)

    print()
    print("You got to the door!")
    win_msg()
    exit_msg()


def walk_along_beach():
    pass


if __name__ == "__main__":
    main()
