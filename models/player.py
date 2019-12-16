class Player:    

    def __init__ (self, pseudo, bag, position):
        """ Cette fonction initialise un player avec un pseudo, un sac vide et une position initiale en haut à gauche."""
        self.pseudo = pseudo
        self.bag = bag
        self.position = position

    def get_bag(self):
        """ Cette fonction renvoit le contenu du sac du joueur. """
        return self.bag