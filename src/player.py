# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name):
        """
        This is constructor function creates all needed variables for instantiation of a new player
        """
        self.current_room = "outside"
        self.name = name

    def set_room(self, room):
        """
        This method sets the new room for the player as they move throughout the game
        """
        self.room = room

    def __str__(self):
        """
        Replacement string method for the Player class
        """
        return f"The current player is {self.name} and they are in {self.room}."

    def __repr__(self):
        """
        REPR method for the Player class
        """
        return f"Player({repr(self.name)})"
