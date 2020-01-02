from . import images
from constants import SPRITE_SIZE
import pygame

class KeeperSprite(pygame.sprite.Sprite): 
    """Déplace un player à travers l'écran. Elle peut faire tournoyer
    le player quand il a attrapé un objet."""
    def __init__(self, keeper, filename):
        super().__init__()        #Appel du constructeur de Sprite
        self.image, self.rect = images.load_image(filename, -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0
        self.keeper = keeper
    
    def update(self):
        "Déplace ou fait tournoyer, suivant l'état du singe"
        self.rect.x = self.keeper.position.x *  SPRITE_SIZE
        self.rect.y = self.keeper.position.y * SPRITE_SIZE