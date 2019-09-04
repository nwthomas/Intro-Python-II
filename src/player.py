# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, item_list):
        """
        This is constructor function creates all needed variables for instantiation of a new player
        """
        self.current_room = "outside"
        self.name = name
        self.item_list = item_list

    def set_room(self, current_room):
        """
        This method sets the new room for the player as they move throughout the game
        """
        self.current_room = current_room

    def print_items(self):
        """
        Prints all items in the items_list
        """
        for item in self.item_list:
            print(f"Item Name: {item.name}, Description: {item.description}")
        print()

    def add_item(self, item):
        """
        Adds in a new item to the player's inventory
        """
        self.item_list.append(item)

    def __getattr__(self, name):
        """
        Defaults to None for any attribute not in the class currently
        """
        return None

    def __str__(self):
        """
        Replacement string method for the Player class
        """
        return f"Name: {self.name}, Room: {self.room}, Items: {self.item_list}."

    def __repr__(self):
        """
        REPR method for the Player class
        """
        return f"Player({repr(self.name)}, {repr(self.item_list)})"
