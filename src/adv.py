from room import Room
from player import Player
import sys

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("What is your name? ")
p = Player(player_name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print(f"\nReady {p.name}")

done = False

while done is False:
    print(f"\nYou are currently in {room[p.current_room].name}.")
    print(room[p.current_room].description)

    try:
        selection = input("Would you like to head n, s, e, or w (or exit)? ")
        new_room = None

        if selection.lower() == "exit":
            print("\nThanks for playing!\n")
            done = True
            continue
        elif selection.lower() == "n":
            new_room = room[p.current_room].n_to
        elif selection.lower() == "s":
            new_room = room[p.current_room].s_to
        elif selection.lower() == "e":
            new_room = room[p.current_room].e_to
        elif selection.lower() == "w":
            new_room = room[p.current_room].w_to
        else:
            print("\nPlease enter n, s, e, w, or exit.")
            continue

        if new_room.name == "Outside Cave Entrance":
            p.set_room("outside")
        elif new_room.name == "Foyer":
            p.set_room("foyer")
        elif new_room.name == "Grand Overlook":
            p.set_room("overlook")
        elif new_room.name == "Narrow Passage":
            p.set_room("narrow")
        elif new_room.name == "Treasure Chamber":
            p.set_room("treasure")
        else:
            print("\nYou must select a valid direction.")

        print(p.current_room)

    except:
        print("\nThat is not a valid input.")
        continue
