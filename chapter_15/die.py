from random import randint

class Die():
    """A class representing a single die"""

    def __init__(self, num_sides=6):
        """The assumption that dice are cube-shaped"""
        self.num_sides = num_sides

    def roll(self):
        """Return a value between 1 and the number of faces the die has"""
        return randint(1, self.num_sides)