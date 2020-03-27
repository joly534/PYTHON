import pygame

pygame.init()
game = True
pygame.display.set_mode((1280, 720)) 

while game :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    