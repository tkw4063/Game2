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

pygame.init()
pygame.display.set_caption("Game 2")
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 650
screen = pygame.display.set_mode(SCREEN_SIZE)

from backgroundmove import backmove

def main(background_pos,pos,universal_speed,player,dinog,r,rcount,scount):
    pressed_keys = pygame.key.get_pressed()

    pos = player.movement(pressed_keys,background_pos,pos)

    background_pos = backmove(screen,pressed_keys,background_pos,universal_speed)

    #print("bg pos: " + str(background_pos))
    rockgr = pygame.sprite.Group()
    spacem = pygame.sprite.Group()
    dinosaur = pygame.sprite.Group()
    spacem.add(player)

    dinog.dmove(pressed_keys,background_pos)
    dinosaur.add(dinog)

    spacem.draw(screen)
    dinosaur.draw(screen)

    r.movement(pressed_keys,background_pos)
    rockgr.add(r)

    if pygame.sprite.groupcollide(spacem,dinosaur,False,False):
        Trust(screen,font,scount)

    if pos > 104.0 and pos < 179.0 and rcount > 0:
        rcount, scount = sodacounting(rcount,screen,scount,player)

    if pygame.sprite.groupcollide(spacem,rockgr,False,True):
        rcount = rockcounting(pressed_keys,background_pos,rockgr,spacem,rcount)
        r = initrocks(background_pos)

    #print(str(rcount))

    inventory(screen,rcount,scount)

    rockgr.draw(screen)

    pygame.display.flip()
