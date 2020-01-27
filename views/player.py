from .images import load_image
from constants import SPRITE_SIZE
import pygame

class PlayerSprite(pygame.sprite.Sprite): 
    """kk"""
    
    def __init__(self, player, filename):
        super().__init__()      #Appel du constructeur de Sprite
        self.image, self.rect = load_image(filename, -1)
        self.player = player
        self.bag = 0
    
    def update(self):
        "jj"
        self.rect.x = self.player.position.x * SPRITE_SIZE
        self.rect.y = self.player.position.y * SPRITE_SIZE

#     def _spin(self):
#         """spin the monkey image"""
#         center = self.rect.center
#         self.dizzy = self.dizzy + 12
#         if self.dizzy >= 360:
#             self.dizzy = 0
#             self.image = self.original
#         else:
#             rotate = pygame.transform.rotate
#             self.image = rotate(self.original, self.dizzy)
#         self.rect = self.image.get_rect(center=center)


#     def get_items(self, target):
#         """catch items and returns the number of items in the bag"""
#         if self.rect == items.rect
#             self._spin()
#         else:
#             self._update()
#         self.bag += 1
#         return self.bag """
        
# """         def _walk(self):
#     """move the monkey across the screen, and turn at the ends"""
#     newpos = self.rect.move((self.move, 0))
#     if not self.area.contains(newpos):
#         if self.rect.left < self.area.left or self.rect.right > self.area.right:
#             self.move = -self.move
#             newpos = self.rect.move((self.move, 0))
#             self.image = pygame.transform.flip(self.image, 1, 0)
#         self.rect = newpos