class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        """
        Used to perform business logic when the item is picked up by the player
        """
        print("\n*************************************************")
        print(f"\nYou have picked up {self.name}.")

    def on_drop(self):
        """
        Used to perform business logic when the item is dropped up by the player
        """
        print("\n*************************************************")
        print(f"\nYou have dropped the {self.name}.")

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
        return f"{self.name} - {self.color}, {self.description}"

    def __repr__(self):
        """
        REPR method for the Lamp class
        """
        return f"Lamp({repr(self.name)}, {repr(self.description)}, {repr(self.color)})"


class Treasure(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description)
        self.value = value

    def __str__(self):
        """
        Replacement string method for the Treasure class
        """
        return f"{self.name} - {self.value}, {self.description}"

    def __repr__(self):
        """
        REPR method for the Treasure class
        """
        return f"Treasure({repr(self.name)}, {repr(self.description)}, {repr(self.value)})"


class Diamond(Treasure):
    def __init__(self, name, description, value, color):
        super().__init__(name, description, value)
        self.color = color

    def __str__(self):
        """
        Replacement string method for the Diamonds class
        """
        return f"{self.name} - {self.value}, {self.color}, {self.description}"

    def __repr__(self):
        """
        REPR method for the Diamonds class
        """
        return f"Diamond({repr(self.name)}, {repr(self.description)}, {repr(self.value)}, {repr(self.color)})"
