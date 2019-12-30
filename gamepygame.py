from models.item import Item
from models.position import Position
from models.player import Player
from models.keeper import Keeper
from models.labyrinth import Labyrinth
from views.images import load_image
from views.items import ItemSprite
from views.keeper import KeeperSprite
from views.player import PlayerSprite
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
        self.player = Player("MacGyver", 0, self.labyrinth.start.get_position(), "resources/MacGyver.png")
        self.keeper = Keeper(copy(self.labyrinth.end), "resources/keeper.png")
        self.tube = Item("Tube", self.labyrinth.random_pos(0), "resources/tube.png")
        self.ether = Item("Ether", self.labyrinth.random_pos(1), "resources/ether.png")
        self.needle = Item("Needle", self.labyrinth.random_pos(2), "resources/needle.png")

    def start(self):
        self.running = True
        pygame.display.set_caption('Labyrinthe MacGyver')
        pygame.mouse.set_visible(0)
        clock = pygame.time.Clock()
        clock.tick(60)

        # We create our window and fill it with maroon
        screen = pygame.display.set_mode((self.labyrinth.width*SPRITE_SIZE, self.labyrinth.length*SPRITE_SIZE))
        screen.fill((153,101,21))
        # On créé le fond de notre labyrinthe
        background = pygame.Surface((self.labyrinth.width*SPRITE_SIZE, self.labyrinth.length*SPRITE_SIZE))
        background.fill(COLOR_MAROON)
        # On créé les chemins
        path = pygame.Surface((SPRITE_SIZE, SPRITE_SIZE))
        path.fill(COLOR_GREEN)
        for position in self.labyrinth.paths:
            background.blit(path, (position.y * SPRITE_SIZE, position.x * SPRITE_SIZE))


        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move(u)  
                    elif event.key == pygame.K_DOWN:
                        self.player.move(d)       
                    elif event.key == pygame.K_RIGHT:
                        self.player.move(r)            
                    elif event.key == pygame.K_LEFT:
                        self.player.move(l)         

        playersprite = PlayerSprite(self.player, "resources/player.png")
        keepersprite = KeeperSprite(self.keeper, "resources/keeper.png")
        allsprites = pygame.sprite.RenderPlain((playersprite, keepersprite))
        allsprites.update()

        # Draw Everything
        allsprites.draw(screen)
        screen.blit(background, (0, 0))
        pygame.display.flip()


def main():
    jeu = Game()
    jeu.start()

if __name__ == '__main__':
    main()