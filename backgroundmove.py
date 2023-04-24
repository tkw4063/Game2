import pygame, sys, os, random

bg = pygame.image.load("mars.jpg")
shuttle = pygame.image.load("spaceshuttle.png").convert_alpha()
shuttle = pygame.transform.scale(shuttle,(600,600))
inside = pygame.image.load("inside.png").convert_alpha()
inside = pygame.transform.scale(inside,(200,200))
rep = pygame.image.load("replicator.jpg")

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

class repl(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super(repl,self).__init__()
        defaultimagesize = (75,75)
        self.image = pygame.image.load("replicator.jpg")#.convert_alpha()
        self.image = pygame.transform.scale(self.image,defaultimagesize)
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def movement(self,pressed_keys,background_pos):
        speed = 2
        #print(str(self.rect.x))
        if pressed_keys[pygame.K_LEFT] and background_pos>0:
            self.rect.x -= speed
        if pressed_keys[pygame.K_RIGHT] and background_pos<-900:
            self.rect.x += speed

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

    repgp = pygame.sprite.Group()
    rep = repl(160,350)
    rep.movement(pressed_keys,background_pos)
    repgp.add(rep)
    repgp.draw(screen)
    return background_pos, repgp
