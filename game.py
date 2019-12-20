from models.item import Item
from models.position import Position
from models.player import Player
from models.garde import Garde
from models.labyrinth import Labyrinth

import random
from copy import copy

class Game:
    def __init__(self):
        """ Cette fonction initie le jeu avec un labyrinthe, un joueur, un garde et 3 items éparpillés. """
        self.running = False
        self.labyrinth = Labyrinth()
        self.labyrinth.define_path("map.txt")
        self.player = Player("MacGyver", 0, copy(self.labyrinth._start))
        self.garde = Garde(self.labyrinth._end)
        self.items_positions = self.labyrinth.random_pos()
        self.items = [
            Item("une aiguille", self.items_positions[0]), 
            Item("un petit tube en plastique", self.items_positions[1]), 
            Item("de l'éther", self.items_positions[2])
        ] 

    def catch_item(self):
        if self.player.position in self.items_positions:
            self.player.bag += 1
            print("Bravo, vous avez " + str(self.player.bag) + " objet(s).")

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
            position_initiale = copy(self.player.position)
            print( "\nVotre position est : " + str(position_initiale))
            print("Les objetcs son s")

            direction = str(input("Où voulez-vous aller ? \n Tapez 'u' 'd' 'l' ou 'r' "))
            self.player.position.update(direction)            
            if self.player.position in self.labyrinth._paths:
                print("\nVous pouvez avancer !")
            else:
                print("\nCe chemin n'est pas autorisé !")
                self.player.position = position_initiale
            print("Votre position est maintenant : " + str(self.player.position))

def main():
    jeu = Game()
    jeu.start()

if __name__ == '__main__':
    main()