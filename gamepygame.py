from models.item import Item
from models.position import Position
from models.player import Player
from models.garde import Garde
from models.labyrinth import Labyrinth
from constants import SPRITE_SIZE, COLOR_MAROON, COLOR_GREEN

import random
import pygame, os, time
from copy import copy

from pygame import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class Game:
    def __init__(self):
        """ Cette fonction initie le jeu avec un labyrinthe, un joueur, un garde et 3 items éparpillés. """
        pygame.init()
        self.running = False
        self.labyrinth = Labyrinth()
        self.labyrinth.define_path("map.txt")
        self.player = Player("MacGyver", 0, copy(self.labyrinth.start), "ressource/MacGyver.png")
        # We create our window and fill it with maroon
        self.screen = pygame.display.set_mode((self.labyrinth.width*SPRITE_SIZE, self.labyrinth.length*SPRITE_SIZE))
        self.screen.fill(COLOR_MAROON)
        # On créé le fond de notre labyrinthe
        background = pygame.Surface((self.labyrinth.width*SPRITE_SIZE, self.labyrinth.length*SPRITE_SIZE))
        self.screen.blit(background, (0, 0))
        # On créé les chemins
        path = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
        path.fill(COLOR_GREEN)
        for position in self.labyrinth.paths:
            background.blit(path, (position.y * SPRITE_SIZE, position.x * SPRITE_SIZE))
        self.screen.blit(background, (0, 0))

        clock = pygame.time.Clock()
        clock.tick(60)

    def start(self):
        pygame.display.flip()
        pygame.display.set_caption('Test program for get_rect()')
        # On créé nos perso et on les assigne à des sprites
        player_img = pygame.image.load("ressource/MacGyver.png").convert_alpha()
        garde_img = pygame.image.load("ressource/Gardien.png").convert_alpha()
        aiguille_img = pygame.image.load("ressource/aiguille.png").convert_alpha()
        ether_img = pygame.image.load("ressource/ether.png").convert_alpha()
        tube_img = pygame.image.load("ressource/tube_plastique.png").convert_alpha()
        player_rect = player_img.get_rect()
        garde_rect = garde_img.get_rect()
        aiguille_rect = aiguille_img.get_rect()
        ether_rect = ether_img.get_rect()
        tube_rect = tube_img.get_rect()
        background.blit(player_rect, (self.labyrinth.start))
        background.blit(garde_rect, (self.labyrinth.end))
        background.blit(aiguille_rect, (self.labyrinth.aiguille.position))
        background.blit(ether_rect, (self.labyrinth.start))
        background.blit(tube_rect, (self.labyrinth.start))

        self.running = True

        while self.running: 
            position_initiale = copy(self.player.position)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.key == K_ESCAPE:
                    self.running = False      
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.position.update(u)            
                        #Voyons si nous sommes sur la case de sortie
                        self.player.exit()
                        # Voyons s'il y a un objet sur cette position
                        self.player.catch_item()
                        # Faisons avancer MacGyver si la direction invite à une position valide
                        if self.player.position in self.labyrinth.paths:
                            rect.move_ip(0, -32)
                        else:
                            self.player.position = position_initiale
                    elif event.key == pygame.K_DOWN:
                        self.player.position.update(u)            
                        self.player.exit()
                        self.player.catch_item()
                        if self.player.position in self.labyrinth.paths:
                            rect.move_ip(0, 32)
                        else:
                            self.player.position = position_initiale
                    elif event.key == pygame.K_RIGHT:
                        self.player.position.update(u)            
                        self.player.exit()
                        self.player.catch_item()
                        if self.player.position in self.labyrinth.paths:
                            rect.move_ip(32, 0)
                        else:
                            self.player.position = position_initiale
                    elif event.key == pygame.K_LEFT:
                        self.player.position.update(u)            
                        self.player.exit()
                        self.player.catch_item()
                        if self.player.position in self.labyrinth.paths:
                            rect.move_ip(-32, 0)
                        else:
                            self.player.position = position_initiale
                pygame.display.update(player_rect)

                        
                # Then blit (add to the buffer) our surface with our rectangle on
                screen.blit(path, (0, 0))
                screen.blit(player, player.position)
                screen.blit(garde, garde.position)
                screen.blit(item1, item1.position)
                screen.blit(item2, item2.position)
                screen.blit(item3, item3.position)
                # Then update the display to show the buffer


def main():
    jeu = Game()
    jeu.start()

if __name__ == '__main__':
    main()