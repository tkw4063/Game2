import pygame, sys, os, random

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)


class man(pygame.sprite.Sprite):
    def __init__(self,speed,defaultimagesize):
        super(man,self).__init__()
        self.speed = speed
        self.image = pygame.image.load("spaceman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 230
        self.rect.y = 410
        self.x = 230
        self.y = 410

    def movement(self,pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys[K_RIGHT]:
            self.x = self.x + self.speed
            self.rect.x = self.x
            # self.rect.move_ip(1,0)
        if pressed_keys[K_LEFT]:
            self.x = self.x - self.speed
            self.rect.x = self.x
            # self.rect.move_ip(-1,0)


        # Keep player on the screen
        if self.rect.top <= 350:
            self.rect.top = 350
        if self.rect.bottom >= 650:
            self.rect.bottom = 650
