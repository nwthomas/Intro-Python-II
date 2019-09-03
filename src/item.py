class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        """
        Replacement string method for the Item class
        """
        return f"Name: {self.name}, Description: {self.description}."

    def __repr__(self):
        """
        REPR method for the Item class
        """
        return f"Item({repr(self.name)}, {repr(self.description)})"
