import pygame, sys, os, random
import spaceman
import dino
from trust import Trust
import rocks

#dir = "~/Game2/"

#Standard sizes
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 650
imagesize = (90,125)
bg = pygame.image.load("mars.jpg")
pygame.font.init()
font = pygame.font.SysFont("Comic Sans MS", 20)
# Import locals for key binding
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

universal_speed = 2
background_speed = universal_speed
background_pos = 0
pygame.init()
pygame.display.set_caption("Game 2")
screen = pygame.display.set_mode(SCREEN_SIZE)

player = spaceman.man(universal_speed,imagesize)
dinog = dino.Dino(universal_speed,background_pos)
shuttle = pygame.image.load("spaceshuttle.png").convert_alpha()
shuttle = pygame.transform.scale(shuttle,(600,600))
inside = pygame.image.load("inside.png").convert_alpha()
inside = pygame.transform.scale(inside,(200,200))

count = 0 #trust count

x = random.randrange(500,800)
y = random.randrange(450,640)
r = rocks.Rocks(x,y)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pressed_keys = pygame.key.get_pressed()

    player.movement(pressed_keys)
    spacem = pygame.sprite.Group()
    spacem.add(player)
    dinosaur = pygame.sprite.Group()
    rockgr = pygame.sprite.Group()

    if pressed_keys[pygame.K_LEFT]:
        background_pos += background_speed
    elif pressed_keys[pygame.K_RIGHT]:
        background_pos -= background_speed

    if background_pos > 0:
        background_pos = 0
    elif background_pos < -900:
        background_pos = -900

    screen.blit(bg,(background_pos,-100))
    screen.blit(shuttle,(background_pos-50,75))
    screen.blit(inside,(background_pos+150,320))

    print("bg pos: " + str(background_pos))

    # dinog.movement(pressed_keys)
    # dinosaur.add(dinog)
    #
    spacem.draw(screen)
    # dinosaur.draw(screen)
    #
    # r.movement(pressed_keys)
    # rockgr.add(r)
    #
    # if pygame.sprite.groupcollide(spacem,dinosaur,False,False):
    #     Trust(screen,font,count)
    #
    # if pygame.sprite.groupcollide(spacem,rockgr,False,True):
    #     count +=1
    #     x = random.randrange(100,500)
    #     y = random.randrange(340,640)
    #     r = rocks.Rocks(x,y)
    #     rockgr.add(r)
    #
    # rockgr.draw(screen)
    pygame.display.flip()
