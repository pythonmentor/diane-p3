
import pygame, os, time
from pygame import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

pygame.display.set_caption('Labyrinthe MacGyver')
pygame.mouse.set_visible(0)
clock = pygame.time.Clock()

# On créé le fond de notre labyrinthe
background = pygame.Surface((15*32,5*32))
background.fill((255,255,255))



while True:
    clock.tick(30)
    screen = pygame.display.set_mode((15 * 32, 5 * 32))
    screen.fill((153,101,21))
    for event in pygame.event.get():
        if event.type == QUIT:
          break
        screen.blit(background, (0, 0))
        pygame.display.flip()
        break

