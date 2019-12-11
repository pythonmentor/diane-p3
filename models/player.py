class Player:    

    def __init__ (self, pseudo, position):
        """ Cette fonction initialise un player avec un pseudo, un ac vide et une position initiale en haut à gauche."""

        self.pseudo = pseudo
        self.bag = []
        self.position = [0, 0]

    def get_bag(self, bag):
        """ Cette fonction renvoit le contenu du sac du joueur. """

        return self.bag

    def get_position(self):
        """ Cette fonction renvoit la position du joueur. """
        
            return self.position