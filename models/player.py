from copy import copy
import pygame

from models.position import Position
from models.item  import Item
from models.labyrinth import Labyrinth

class Player:    

    def __init__ (self, pseudo, bag, position, jeu):
        """ Cette fonction initialise un player avec un pseudo, un sac vide et une position"""
        self.pseudo = pseudo
        self.bag = bag
        self.position = position
        self.jeu = jeu

    def catch_item(self):
        if self.position in self.jeu.labyrinth.items_positions:
            self.player.bag += 1
            print("Bravo, vous avez " + str(self.player.bag) + " objet(s).")
        else:
            pass

    def exit(self):
        if self.position == self.jeu.labyrinth.end:
            if self.bag == 3:
                print("Bravo, vous avez pu endormir le garde et sortir du labyrinthe, vous avez gagné !")
            else:
                print("Et non, il vous manquait un ou des objets, perdu")
                pygame.QUIT
        else:
            pass

    def move(self, direction, paths):
        # Voyons si la direction invite à une position valide
        prev_position = copy(self.position)
        self.position.update(direction)
        if self.position in paths:
            #Voyons si nous sommes sur la case de sortie
            self.exit()
            # punch_sound = load_sound("punch.wav")
            # punch_sound.play() 
            # Voyons s'il y a un objet sur cette position
          #  self.catch_item()
            # whiff_sound = load_sound("whiff.wav")
            # whiff_sound.play() 
            # Faisons avancer MacGyver 
        else:
            self.position = prev_position