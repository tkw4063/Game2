import pygame, sys, os, random

bg = pygame.image.load("mars.jpg")
shuttle = pygame.image.load("spaceshuttle.png").convert_alpha()
shuttle = pygame.transform.scale(shuttle,(600,600))
inside = pygame.image.load("inside.png").convert_alpha()
inside = pygame.transform.scale(inside,(200,200))

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

def backmove(screen,pressed_keys,background_pos,background_speed):
    if pressed_keys[pygame.K_LEFT]:
        background_pos += background_speed
    elif pressed_keys[pygame.K_RIGHT]:
        background_pos -= background_speed

    if background_pos > 0:
        background_pos = 0
    elif background_pos < -900:
        background_pos = -900


    screen.blit(bg,(background_pos,-100))
    screen.blit(shuttle,(background_pos-50,75))
    screen.blit(inside,(background_pos+150,320))
    return background_pos
