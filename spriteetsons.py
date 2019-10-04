import pygame, sys, time, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT, 0, 32)