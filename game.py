from models.item import Item
from models.position import Position
from models.player import Player
from models.garde import Garde
from models.labyrinth import Labyrinth

import random

class Game:
    def __init__(self):
        """ Cette fonction initie le jeu avec un labyrinthe, un joueur, un garde et 3 items éparpillés. """
        self.running = False
        self.labyrinth = Labyrinth()
        self.labyrinth.define_path("labyrinth.txt")
        self.player = Player("MacGyver", 0, self.labyrinth.start)
        self.garde = Garde(self.labyrinth.end)
        self.items = [
            Item("une aiguille", self.labyrinth.paths[0]), 
            Item("un petit tube en plastique", self.labyrinth.paths[1]), 
            Item("de l'éther", self.labyrinth.paths[2])
        ] 
    
    def is_valid_position(self, position):
        self.position in self.labyrinth._paths

"""     def catch_item(self):
        if self.player.position == self.items
            print("Bravo, vous avez attrapé " + str(self.player.bag) + " objet(s).") """

    def exit(self):
        if self.player.position == (14,14) and self.player.bag == 3:
            print("Bravo, vous avez pu endormir le garde!")
        elif self.player.position == (14,14) and self.player.bag == 2:
            print("Et non, il vous manquait un objet, perdu") #exit game
        elif self.player.position == (14,14) and self.player.bag == 1:
            print("Et non, il vous manquait un objet, perdu") #exit game
        else:
            pass

    def start(self):
        self.running = True
        while self.running:
            direction = str(input("Where would you like to go ? R, L, U or D(down)"))
            position_initiale = self.player.position.copy()
            self.player.position.update(direction)
            if self.player.position not in self.labyrinth.paths:
                self.player.position = position_initiale
                print("Ce chemin n'est pas autorisé!")

            

        print("Votre position est mantenant : x = " + str(self.player.position.x) + " et y = "+ str(self.player.position.y))

def main():
    jeu = Game()
    jeu.start()

if __name__ == '__main__':
    main()


