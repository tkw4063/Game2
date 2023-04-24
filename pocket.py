import pygame, sys, os, random
from textobj import text_objects

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

def inventory(screen,rcount,scount):
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(900,0,960,70))

    title, TextRect1 = text_objects("Inventory",font)
    rock, TextRect2 = text_objects("Rocks: "+str(rcount),font)
    soda, TextRect3 = text_objects("BC Cola: "+str(scount),font)
    TextRect1.center = ((950),(10))
    TextRect2.center = ((950),(35))
    TextRect3.center = ((950),(60))
    screen.blit(title,TextRect1)
    screen.blit(rock,TextRect2)
    screen.blit(soda,TextRect3)
