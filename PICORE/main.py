import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1280, 720))

fond = pygame.image.load("image/fond.jpg").convert_alpha()
fond_rect = fond.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(fond, fond_rect)
    pygame.display.flip()

    