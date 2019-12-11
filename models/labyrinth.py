import random

from .position import Position

class Labyrinth:

    def __init__(self):
        """ Cette fonction initialise un labyrinthe avec des chemins, une position de départ, d'arrivée, et des murs. """

        self._paths = []
        self._start = None
        self._end = None
        self._walls = []

    def define_path(self, filename):
        """ Cette fonction map les chemins et les positions du labyrinthe en fonction d'un fichier texte. """
        
        with open(filename) as file:
            content = file.readlines()
            for num_line, line in enumerate(content):
                for num_c, c in enumerate(line):
                    if c == "P":
                        self._paths.append(Position(num_c, num_line))
                    elif c == "D":
                        self._start = Position(num_c, num_line)
                    elif c == "A":
                        self._end = Position(num_c, num_line)
                    elif c == "-":
                        self._walls.append(Position(num_c, num_line))
                        
        random.shuffle(self.paths)
        self.paths.append(self.start)
        self.paths.append(self.end)

    def 
