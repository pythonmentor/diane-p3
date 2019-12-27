from models.position import Position
from models.item  import Item
from models.labyrinth import Labyrinth

class Player:    

    def __init__ (self, pseudo, bag, position, filename):
        """ Cette fonction initialise un player avec un pseudo, un sac vide et une position"""
        self.pseudo = pseudo
        self.bag = bag
        self.position = Position(x, y)
        self.filename = filename

    def move(self, direction):
        self.position = position.update(direction)

    def catch_item(self):
        if self.position in labyrinth.items_positions:
            self.player.bag += 1
            print("Bravo, vous avez " + str(self.player.bag) + " objet(s).")
        else:
            pass

    def exit(self):
        if self.position == labyrinth.end:
            if self.bag == 3:
                print("Bravo, vous avez pu endormir le garde et sortir du labyrinthe, vous avez gagné !")
            else:
                print("Et non, il vous manquait un ou des objets, perdu")
                pygame.QUIT
        else:
            pass
            
            
