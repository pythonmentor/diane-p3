import random

class Position: 
    """ Cette classe définit une position."""

    def __init__(self, x, y):
        """ Cette classe donne un x et un y à la position. """

        self.x = x
        self.y = y

    def update(self, direction):
        """ Cette fonction permet de faire évoluer la position d'une case vers une direction."""

        if direction == "r":
            self.x += 1
        elif direction == "l":
            self.x -= 1
        elif direction == "u":
            self.y -= 1
        elif direction == "d":
            self.y += 1

    def get_position(self):
        """ Cette fonction renvoit la position. """

        return Position(self.x, self.y)

    def __eq__(self, other):
        """ Cette fonction permet de comparer si deux positions sont identiques. """

        return self == other

    def __repr__(self):
        """ Cette fonction renvoie la position sous forme x y"""
        
        return f"Position ({self.x}, {self.y})"