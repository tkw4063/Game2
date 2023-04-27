import pygame

def sodacounting(rcount,screen,shitcount,player):
    #print("we're in soda counting and here are the inputs: " + str(rcount) + " " +str(shitcount))
    rcount -= 1
    shitcount += 1
    return rcount, shitcount
