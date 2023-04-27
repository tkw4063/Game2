import pygame, sys, os, random
from textobj import text_objects

def Trust(surface,font,count):
    #print("trust")
    bubble = pygame.image.load("bubble.png").convert_alpha()
    bubble = pygame.transform.scale(bubble,(375,100))

    if count < 5:
        thoughtsurf, thoughtrect = text_objects("I don't trust you, feed me BC Cola",font)
        thoughtrect.center = ((550),(390))
        surface.blit(bubble,((370),(360)))
        surface.blit(thoughtsurf, thoughtrect)
    else:
        thoughtsurf, thoughtrect = text_objects("You are my leader!",font)
        thoughtrect.center = ((550),(390))
        surface.blit(bubble,((370),(360)))
        surface.blit(thoughtsurf, thoughtrect)
    return count
