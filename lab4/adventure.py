#!/usr/bin/env python
#
# A text-based adventure game, based on
# https://github.com/codinggrace/text_based_adventure_game
#
# MIT License
# Copyright (c) 2020 Coding Grace
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

DESCRIPTIONS = {
    "Start": """You enter a room, and you see a blue door to your left and a \
red door to your right.
Which door do you pick?""",
    "Blue": """You see a room with a wooden treasure chest on the left, and a \
sleeping guard on the right in front of the door.
What do you do?""",
    "Chest": """Let's see what's in here... /grins
The chest creaks open, and the guard is still sleeping. That's one heavy \
sleeper! You find some diamonds, a shiny sword, and lots of gold coins.
Do you take the treasure or leave it?""",
    "Take": """Woohoo! Bounty and a shiney new sword. /drops your crappy \
sword in the empty treasure chest.
Ooops! The noise has woken up the guard.
What do you do now?""",
    "Leave":
    """Leaving all the shinies behind hurts, but it feels safer for now.
Hopefully, it will still be here, right after you gets past this guard.
What do you do next?""",
    "Guard": """The guard seems to be deep in sleep, but he has a mean \
looking axe right beside him.
What do you do?""",
    "Sneak": """The guard jumps up and looks the other way, missing you \
entirely.
You just slipped through the door before the guard realised it.
You are now outside, home free! Huzzah!""",
    "Talk": """The guard approaches you and swings his axe, and your world \
goes dark...""",
    "Red": """There you see the great evil Slathborg.
He, it, whatever stares at you and you go insane.
Do you flee for your life or attack it with your bare hands?""",
    "Flee": """You made it out alive, alas empty handed.""",
    "Attack": """You died. Well, at least the dragon thought you were tasty"""
}

OPTIONS = {
    "Blue": "Blue",
    "Red": "Red",
    "Chest": "Explore the chest",
    "Guard": "Advance toward the guard",
    "Take": "Grab all of the treasures",
    "Leave": "Leave them for another day",
    "Sneak": "Try to sneak past the guard",
    "Talk": "Talk to the guard",
    "Flee": "Flee",
    "Attack": "Attack"
}


def print_doors():
    print()
    print(r"   _________________________________________________________ ")
    print(r" /|     -_-                                             _-  |\ ")
    print(r"/ |_-_- _                                         -_- _-   -| \ ")
    print(r"  |                            _-  _--                      | ")
    print(r"  |                            ,                            | ")
    print(r"  |      .-'````````'.        '(`        .-'```````'-.      | ")
    print(r"  |    .` |           `.      `)'      .` |           `.    | ")
    print(r"  |   /   |   ()        \      U      /   |    ()       \   | ")
    print(r"  |  |    |    ;         | o   T   o |    |    ;         |  | ")
    print(r"  |  |    |     ;        |  .  |  .  |    |    ;         |  | ")
    print(r"  |  |    |     ;        |   . | .   |    |    ;         |  | ")
    print(r"  |  |    |     ;        |    .|.    |    |    ;         |  | ")
    print(r"  |  |    |____;_________|     |     |    |____;_________|  | ")
    print(r"  |  |   /  __ ;   -     |     !     |   /     `'() _ -  |  | ")
    print(r"  |  |  / __  ()        -|        -  |  /  __--      -   |  | ")
    print(r"  |  | /        __-- _   |   _- _ -  | /        __--_    |  | ")
    print(r"  |__|/__________________|___________|/__________________|__| ")
    print(r" /                                             _ -        lc \ ")
    print(r"/   -_- _ -             _- _---                       -_-  -_ \ ")
    print()


def print_dragon():
    print()
    print(r"            |                     | ")
    print(r"         \     /               \     / ")
    print(r"        -= .'> =-             -= <'. =- ")
    print(r"           '.'.                 .'.' ")
    print(r"             '.'.             .'.' ")
    print(r"               '.'.----^----.'.' ")
    print(r"                /'==========='\ ")
    print(r"            .  /  .-.     .-.  \  . ")
    print(r"            :'.\ '.O.') ('.O.' /.': ")
    print(r"            '. |               | .' ")
    print(r"              '|      / \      |' ")
    print(r"               \     (o'o)     / ")
    print(r"               |\             /| ")
    print(r"               \('._________.')/ ")
    print(r"                '. \/|_|_|\/ .' ")
    print(r"                 /'._______.'\ lc ")
    print()


def print_treasure():
    print()
    print("                      _.--. ")
    print("                  _.-'_:-'|| ")
    print("              _.-'_.-::::'|| ")
    print("         _.-:'_.-::::::'  || ")
    print("       .'`-.-:::::::'     || ")
    print("      /.'`;|:::::::'      ||_ ")
    print("     ||   ||::::::'     _.;._'-._ ")
    print("     ||   ||:::::'  _.-!oo @.!-._'-. ")
    print("     ('.  ||:::::.-!()oo @!()@.-'_.| ")
    print("      '.'-;|:.-'.&$@.& ()$%-'o.'-U|| ")
    print("        `>'-.!@%()@'@_%-'_.-o _.|'|| ")
    print("         ||-._'-.@.-'_.-' _.-o  |'|| ")
    print("         ||=[ '-._.-+U/.-'    o |'|| ")
    print("         || '-.]=|| |'|      o  |'|| ")
    print("         ||      || |'|        _| '; ")
    print("         ||      || |'|    _.-'_.-' ")
    print("         |'-._   || |'|_.-'_.-' ")
    print("          '-._'-.|| |' `_.-' ")
    print("              '-.||_/.-' ")
    print()


def print_guard():
    print()
    print(r"                        ___I___ ")
    print(r"                       /=  |  #\ ")
    print(r"                      /.__-| __ \ ")
    print(r"                      |/ _\_/_ \| ")
    print(r"                      (( __ \__)) ")
    print(r"                   __ ((()))))()) __ ")
    print(r"                 ,'  |()))))(((()|# `. ")
    print(r"                /    |^))()))))(^|   =\ ")
    print(r"               /    /^v^(())()()v^;'  .\ ")
    print(r"               |__.'^v^v^))))))^v^v`.__| ")
    print(r"              /_ ' \______(()_____(   | ")
    print(r"         _..-'   _//_____[xxx]_____\.-| ")
    print(r"        /,_#\.=-' /v^v^v^v^v^v^v^v^| _| ")
    print(r"        \)|)      v^v^v^v^v^v^v^v^v| _| ")
    print(r"         ||       :v^v^v^v^v^v`.-' |#  \, ")
    print(r"         ||       v^v^v^v`_/\__,--.|\_=_/ ")
    print(r"         ><       :v^v____|  \_____|_ ")
    print(r"      ,  ||       v^      /  \       / ")
    print(r"     //\_||_)\    `/_..-._\   )_...__\ ")
    print(r"    ||   \/  #|     |_='_(     |  =_(_ ")
    print(r"    ||  _/\_  |    /     =\    /  '  =\ ")
    print(r"     \\\/ \/ )/    |=____#|    '=....#| ")
    print()


def print_game_over():
    print()
    print(r"   _____          __  __ ______    ______      ________ _____ ")
    print(r"  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
    print(r" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) | ")
    print(r" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
    print(r" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
    print(r"  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ")
    print()


name = input("What's your name?\n>> ")
print("Welcome {} to the adventure of your life. Try to survive and find the \
treasure!".format(name.upper()))
text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS["Start"],
                                       "1", OPTIONS["Blue"],
                                       "2", OPTIONS["Red"])
print_doors()
print(text_box)
inp = input(">> ")

if inp == "1":
    text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS["Blue"],
                                           "1", OPTIONS["Chest"],
                                           "2", OPTIONS["Guard"])
    print(text_box)
    inp = input(">> ")

    if inp == "1":
        text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS["Chest"],
                                               "1", OPTIONS["Take"],
                                               "2", OPTIONS["Leave"])
        print_treasure()
        print(text_box)
        inp = input(">> ")

        if inp == "1":
            text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS["Take"],
                                                   "1", OPTIONS["Sneak"],
                                                   "2", OPTIONS["Talk"])
            print(text_box)
            inp = input(">> ")

            if inp == "1":
                text_box = "{}".format(DESCRIPTIONS["Sneak"])
                print_guard()
                print(text_box)

            elif inp == "2":
                text_box = "{}".format(DESCRIPTIONS["Talk"])
                print_guard()
                print(text_box)
                print_game_over()

        elif inp == "2":
            text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS["Leave"],
                                                   "1", OPTIONS["Sneak"],
                                                   "2", OPTIONS["Talk"])
            print(text_box)
            inp = input(">> ")

            if inp == "1":
                text_box = "{}".format(DESCRIPTIONS["Sneak"])
                print_guard()
                print(text_box)

            elif inp == "2":
                text_box = "{}".format(DESCRIPTIONS["Talk"])
                print_guard()
                print(text_box)
                print_game_over()

    elif inp == "2":
        text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS["Guard"],
                                               "1", OPTIONS["Sneak"],
                                               "2", OPTIONS["Talk"])
        print(text_box)
        inp = input(">> ")

        if inp == "1":
            text_box = "{}".format(DESCRIPTIONS["Sneak"])
            print_guard()
            print(text_box)

        elif inp == "2":
            text_box = "{}".format(DESCRIPTIONS["Talk"])
            print_guard()
            print(text_box)
            print_game_over()

elif inp == "2":
    text_box = "{}\n{}  {}\n{}  {}".format(DESCRIPTIONS["Red"],
                                           "1", OPTIONS["Flee"],
                                           "2", OPTIONS["Attack"])
    print_dragon()
    print(text_box)
    inp = input(">> ")

    if inp == "1":
        text_box = "{}".format(DESCRIPTIONS["Flee"])
        print(text_box)

    elif inp == "2":
        text_box = "{}".format(DESCRIPTIONS["Attack"])
        print(text_box)
        print_game_over()
