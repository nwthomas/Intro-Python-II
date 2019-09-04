# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item_list):  # add back in item_list
        self.name = name
        self.description = description
        self.item_list = item_list

    def get_name(self):
        """
        Returns the name of the instantiated Room class
        """
        return self.name

    def __getattr__(self, name):
        return None

    def __str__(self):
        """
        Replacement string method for the Room class
        """
        return f"Name: {self.name}, Description: {self.description}, Items: {self.item_list}"

    def __repr__(self):
        """
        REPR method for the Room class
        """
        return f"Room({repr(self.name)}, {repr(self.description)}, {repr(self.item_list)})"
