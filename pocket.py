import pygame, sys, os, random
from textobj import text_objects

pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)

def inventory(screen,rcount,scount,dcount):
    pygame.draw.rect(screen,(255,255,255),pygame.Rect(880,0,960,100))

    title, TextRect1 = text_objects("Inventory",font)
    rock, TextRect2 = text_objects("Rocks: "+str(rcount),font)
    soda, TextRect3 = text_objects("BC Cola: "+str(scount),font)
    din, TextRect4 = text_objects("Followers: " + str(dcount),font)
    TextRect1.center = ((940),(10))
    TextRect2.center = ((940),(35))
    TextRect3.center = ((940),(60))
    TextRect4.center = ((940),(85))
    screen.blit(title,TextRect1)
    screen.blit(rock,TextRect2)
    screen.blit(soda,TextRect3)
    screen.blit(din,TextRect4)
