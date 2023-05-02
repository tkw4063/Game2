import random
import rocks
import pygame

def initrocks(background_pos):
    x = random.randrange(500,900)
    if background_pos < 0:
        x = x+background_pos
    y = random.randrange(450,600)
    r = rocks.Rocks(x,y)
    return r
