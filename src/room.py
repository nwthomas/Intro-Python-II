# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item_list):  # add back in item_list
        self.name = name
        self.description = description
        self.item_list = item_list

    def print_items(self):
        """
        Prints all items in the items list
        """
        for item in self.item_list:
            print(f"Item Name: {item.name}, Description: {item.description}")
        print()

    def __getattr__(self, name):
        """
        Defaults to None for any attribute not in the class currently
        """
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
