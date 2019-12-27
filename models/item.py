
class Item:
    def __init__(self, name, position, filename):
        self.name = name
        self.position = position
        self.filename = filename

    def random_pos(self, number):
        """ Cette fonction renvoit une position aléatoire qui n'est ni l'arrivée ni le départ. """
        list = random.sample(labyrinth.paths[:-2], 3)
        self.position = list[number]