from models.position import Position
from models.item import Item

import random

class Labyrinth:

    def __init__(self):
        """ Cette fonction initialise un labyrinthe avec des chemins, une position de départ, d'arrivée, et des murs. """

        self.paths = []
        self.start = None
        self.end = None
        self.walls = []
        self.bar = []

    def define_path(self, filename):
        """ Cette fonction map les chemins et les positions du labyrinthe en fonction d'un fichier texte. """
        
        with open(filename) as file:
            content = file.readlines()
            for num_line, line in enumerate(content):
                for num_c, c in enumerate(line):
                    if c == "P":
                        self.paths.append(Position(num_c, num_line))
                    elif c == "D":
                        self.start = Position(num_c, num_line)
                    elif c == "A":
                        self.end = Position(num_c, num_line)
                    elif c == "-":
                        self.walls.append(Position(num_c, num_line))
                    elif c == "#":
                        self.bar.append(Position(num_c, num_line))
        self.width = num_c + 1
        self.length = num_line + 1
                
        self.paths.append(self.end)
        self.paths.append(self.start)
    
    def random_pos(self, number):
        """ This gives a position in paths that is neither the beginning nor the end. """
        positions = random.sample(self.paths[:-2], 3)
        return positions[number]