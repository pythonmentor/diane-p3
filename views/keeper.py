from . import images
from constants import SPRITE_SIZE
import pygame

class KeeperSprite(pygame.sprite.Sprite): 
    """Déplace un player à travers l'écran. Elle peut faire tournoyer
    le player quand il a attrapé un objet."""
    def __init__(self, keeper, filename):
        super().__init__()        #Appel du constructeur de Sprite
        self.image, self.rect = images.load_image(filename, -1)
        self.keeper = keeper
        self.rect.x = self.keeper.position.x * SPRITE_SIZE
        self.rect.y = self.keeper.position.y * SPRITE_SIZE