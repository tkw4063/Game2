import pygame, sys, os, random
import rocks
from rockdraw import initrocks
from textobj import text_objects

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

def rockcounting(pressed_keys,background_pos,rockgr,spacem,rrcount):
    #print("we're in rock counting and here are the inputs: " + str(rrcount))
    rrcount = rrcount + 1

    return rrcount
