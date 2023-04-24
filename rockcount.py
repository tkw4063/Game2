import pygame, sys, os, random
import rocks
from rockdraw import initrocks
from textobj import text_objects

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

def rockcounting(pressed_keys,background_pos,r,rockgr,spacem,rcount):
    r.movement(pressed_keys,background_pos)
    rockgr.add(r)

    if pygame.sprite.groupcollide(spacem,rockgr,False,True):
        rcount +=1
        rockgr = pygame.sprite.Group()
        r = initrocks(background_pos)

    return r,rcount,rockgr

def sodacounting(screen,rcount,scount,spacem,repgp):
    if pygame.sprite.groupcollide(spacem,repgp,False,False):
        if rcount == 0:
            text,trect = text_objects("You need rocks",font)
            trect.center = ((100),(300))
            screen.blit(text,trect)
        elif rcount !=0:
            rcount = rcount - 1
            scount = scount + 1

    return rcount, scount
