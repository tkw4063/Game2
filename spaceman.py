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
        self.speed = 1.5 #speed
        self.image = pygame.image.load("spaceman.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((0,0,0))
        self.rect = self.image.get_rect()
        self.x = 230
        self.y = 410
        self.rect.x = 230
        self.rect.y = 410

    def movement(self,pressed_keys,background_pos):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0,-1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,1)
        if pressed_keys[K_RIGHT] and background_pos==-900:
            self.x = self.x + self.speed
            self.rect.x = self.x
        if pressed_keys[K_LEFT] and background_pos==0:
            self.x = self.x - self.speed
            self.rect.x = self.x

        #print(str(self.rect.x))

        # Keep player on the screen
        if self.rect.top <= 350:
            self.rect.top = 350
        if self.rect.bottom >= 650:
            self.rect.bottom = 650
        if self.rect.x<=-40:
            self.rect.x =-40
        if self.rect.x>=922:
            self.rect.x =922
