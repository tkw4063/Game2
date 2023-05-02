import pygame, sys, os, random
from textobj import text_objects
import dino

def Trust(surface,font,count,dcount,universal_speed,background_pos):
    #print("trust")
    bubble = pygame.image.load("bubble.png").convert_alpha()
    bubble = pygame.transform.scale(bubble,(375,100))

    if count < 5:
        pygame.time.delay(200)
        thoughtsurf, thoughtrect = text_objects("I don't trust you, feed me BC Cola",font)
        thoughtrect.center = ((550),(390))
        surface.blit(bubble,((370),(360)))
        surface.blit(thoughtsurf, thoughtrect)
    if count >=5:
        count -= 5
        dcount +=1
        dinog = dino.Dino(universal_speed,background_pos)
    return count, dcount
