import pygame, sys, os, random
import rocks
from rockdraw import initrocks

def rockcounting(pressed_keys,background_pos,r,rockgr,spacem,rcount):
    r.movement(pressed_keys,background_pos)
    rockgr.add(r)

    if pygame.sprite.groupcollide(spacem,rockgr,False,True):
        rcount +=1
        rockgr = pygame.sprite.Group()
        r = initrocks(background_pos)

    return r,rcount,rockgr
