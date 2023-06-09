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
from backgroundmove import backmove
from textobj import text_objects

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

def main(screen,universal_speed,background_pos,pos,player,dinog,rcount,scount,r,dcount):
    cond = True
    while cond:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
            scount, dcount = Trust(screen,font,scount,dcount,universal_speed,background_pos)

        if pos > 104.0 and pos < 179.0 and rcount > 0:
            rcount, scount = sodacounting(rcount,screen,scount,player)

        if pygame.sprite.groupcollide(spacem,rockgr,False,True):
            rcount = rockcounting(pressed_keys,background_pos,rockgr,spacem,rcount)
            r = initrocks(background_pos)

        #print(str(rcount))

        inventory(screen,rcount,scount,dcount)

        rockgr.draw(screen)

        pygame.display.flip()
