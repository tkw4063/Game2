import pygame, sys, os, random
from textobj import text_objects

def button(screen,msg,x,y,w,h,ic,ac,action=None):
    pygame.font.init()
    font = pygame.font.SysFont("Comic Sans MS", 20)
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    # Changing the color when mouse hovers over it
    if x+w > mouse[0] > x and y+h > mouse[1] >y:
        pygame.draw.rect(screen,ac,(x,y,w,h))
        if click[0] == 1 and action !=None:
            action()
    else:
        pygame.draw.rect(screen,ic,(x,y,w,h))

    textSurf,textRect = text_objects(msg,font)
    textRect.center = ((x+(w/2)),(y+(h/2)))
    screen.blit(textSurf,textRect)
