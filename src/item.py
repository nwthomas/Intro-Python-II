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
