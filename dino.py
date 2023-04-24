import pygame, sys, os, random
import textobj

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class Dino(pygame.sprite.Sprite):
    def __init__(self,speed,pressed_keys):
        super(Dino,self).__init__()
        self.speed = speed
        defaultimagesize = (90,125)
        self.image = pygame.image.load("dinosaurleft.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = 1200
        self.rect.y = 400

    def dmove(self,pressed_keys,background_pos):
        self.speed = 2
        defaultimagesize = (90,125)
        if pressed_keys[pygame.K_LEFT] and background_pos<0:
            self.rect.x += self.speed
            self.image = pygame.image.load("dinosaurright.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,defaultimagesize)
            self.image.set_colorkey((255,255,255))
        elif pressed_keys[pygame.K_RIGHT] and background_pos>-900:
            self.rect.x -= self.speed
            self.image = pygame.image.load("dinosaurleft.png").convert_alpha()
            self.image = pygame.transform.scale(self.image,defaultimagesize)
            self.image.set_colorkey((255,255,255))
