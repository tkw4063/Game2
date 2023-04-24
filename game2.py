import pygame, sys, os, random
import spaceman
import dino
from trust import Trust
import rocks
from movement import move
from rockdraw import initrocks
from rockcount import rockcounting
from pocket import inventory


#dir = "~/Game2/"

#Standard sizes
imagesize = (90,125)
pygame.init()
pygame.display.set_caption("Game 2")
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 650
screen = pygame.display.set_mode(SCREEN_SIZE)

from backgroundmove import backmove

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)
# Import locals for key binding
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

universal_speed = 2
background_speed = universal_speed
background_pos = 0

player = spaceman.man(universal_speed,imagesize)
dinog = dino.Dino(universal_speed,background_pos)


rcount = 0 #rock count
scount = 0 #soda count
r = initrocks(background_pos)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pressed_keys = pygame.key.get_pressed()

    player.movement(pressed_keys,background_pos)

    background_pos = backmove(screen,pressed_keys,background_pos,universal_speed)
    inventory(screen,rcount,scount)

    #print("bg pos: " + str(background_pos))
    rockgr = pygame.sprite.Group()
    spacem = pygame.sprite.Group()
    dinosaur = pygame.sprite.Group()
    spacem.add(player)

    dinog.dmove(pressed_keys,background_pos)
    dinosaur.add(dinog)

    spacem.draw(screen)
    dinosaur.draw(screen)

    if pygame.sprite.groupcollide(spacem,dinosaur,False,False):
        Trust(screen,font,scount)

    r,rcount,rockgr = rockcounting(pressed_keys,background_pos,r,rockgr,spacem,rcount)


    rockgr.draw(screen)
    pygame.display.flip()
