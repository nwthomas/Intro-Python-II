class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __getattr__(self, name):
        """
        Defaults to None for any attribute not in the class currently
        """
        return None

    def __str__(self):
        """
        Replacement string method for the Item class
        """
        return f"{self.name} - {self.description}"

    def __repr__(self):
        """
        REPR method for the Item class
        """
        return f"Item({repr(self.name)}, {repr(self.description)})"


class Lamp(Item):
    def __init__(self, name, description, color):
        super().__init__(name, description)
        self.color = color

    def __str__(self):
        """
        Replacement string method for the Lamp class
        """
        return f"{self.color} {self.name} - {self.description}"

    def __repr__(self):
        """
        REPR method for the Lamp class
        """
        return f"Item({repr(self.name)}, {repr(self.description)}, {repr(self.color)})"
