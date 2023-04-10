import pygame, sys, os, random

class Rocks(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(Rocks,self).__init__()
        defaultimagesize = (90,125)
        self.image = pygame.image.load("C:/Users/tkw40/Documents/Clemson/Student/CPCS_6160/Game2/rock.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
