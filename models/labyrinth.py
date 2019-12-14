from position import Position

import random

class Labyrinth:

    def __init__(self):
        """ Cette fonction initialise un labyrinthe avec des chemins, une position de départ, d'arrivée, et des murs. """

        self._paths = []
        self._paths_complets = []
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
        
        random.shuffle(self._paths)
        self._paths_complets.append(self._start)
        self._paths_complets.append(self._end)
        self._paths_complets.append(self._paths)

    
    def random_pos(self):
        """ Cette fonction définit une position aléatoire qui n'est ni l'arrivée ni le départ. """
        random.shuffle(self._paths) 
        return random.choice(self._paths)

lab = Labyrinth()
lab.define_path
yo = lab.random_pos()
print(yo)