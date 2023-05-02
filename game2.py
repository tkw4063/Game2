import pygame, sys, os, random
import spaceman
import dino
from trust import Trust
import rocks
from movement import move
from rockdraw import initrocks
from rockcount import rockcounting
from soda import sodacounting
from pocket import inventory


#dir = "~/Game2/"

#Standard sizes
imagesize = (90,125)
pygame.init()
pygame.display.set_caption("Game 2")
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 650
screen = pygame.display.set_mode(SCREEN_SIZE)

from backgroundmove import backmove
from Main import main

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
pos = 230

player = spaceman.man(universal_speed,imagesize)
dinog = dino.Dino(universal_speed,background_pos)

rcount = 0 #rock count
scount = 0 #soda count
dcount = 0 #dinosaur count
r = initrocks(background_pos)

main(screen,universal_speed,background_pos,pos,player,dinog,rcount,scount,r,dcount)
