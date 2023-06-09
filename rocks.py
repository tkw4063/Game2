import pygame, sys, os, random

class Rocks(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Rocks,self).__init__()
        defaultimagesize = (60,65)
        self.image = pygame.image.load("rock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def movement(self,pressed_keys,background_pos):
        speed = 2
        #print(str(self.rect.x))
        if pressed_keys[pygame.K_LEFT] and background_pos<0:
            self.rect.x += speed
        if pressed_keys[pygame.K_RIGHT] and background_pos>-900:
            self.rect.x -= speed
