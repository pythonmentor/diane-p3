import os
import sys

import pygame

def load_image(name, colorkey=None):
    fullname = os.path.join('resources', name)
    try:
        image = pygame.transform.scale(pygame.image.load(fullname), (50, 50))
    except pygame.error as message:
        print("Impossible de charger l'image :", name)
        raise SystemExit
    image = image.convert_alpha()
    return image, image.get_rect()
"""     if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL) """