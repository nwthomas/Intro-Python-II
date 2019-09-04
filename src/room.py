# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item_list):  # add back in item_list
        self.name = name
        self.description = description
        self.item_list = item_list
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def get_name(self):
        """
        Returns the name of the instantiated Room class
        """
        return self.name

    def __str__(self):
        """
        Replacement string method for the Room class
        """
        return f"Name: {self.name}, Description: {self.description}"

    def __repr__(self):
        """
        REPR method for the Room class
        """
        return f"Room({repr(self.name)}, {repr(self.description)})"
