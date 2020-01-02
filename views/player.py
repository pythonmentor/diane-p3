from .images import load_image
from constants import SPRITE_SIZE
import pygame

class PlayerSprite(pygame.sprite.Sprite): 
    """Déplace un player à travers l'écran. Elle peut faire tournoyer
    le player quand il a attrapé un objet."""
    def __init__(self, player, filename):
        super().__init__()        #Appel du constructeur de Sprite
        self.image, self.rect = load_image(filename, -1)
        """  screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 10, 10
        self.move = 9
        self.dizzy = 0"""
        self.player = player
    
    def update(self):
        "Déplace ou fait tournoyer, suivant l'état du singe"
        self.rect.x = self.player.position.x *  SPRITE_SIZE
        self.rect.y = self.player.position.y * SPRITE_SIZE

    """def _spin(self):
        "Faire tournoyer l'image du singe"
        center = self.rect.center
        self.dizzy += 12
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)"""