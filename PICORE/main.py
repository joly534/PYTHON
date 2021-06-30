import pygame
from player import Player
from game import Game

pygame.init()

#generer la fenetre du jeu
pygame.display.set_caption("Pycore")
screen = pygame.display.set_mode((1280, 720))

background = pygame.image.load("image/fond.jpg")

#on instancie le jeu
game = Game()

#boucle de jeu
while game:

    #appliquer l'arriere plan
    screen.blit(background, (0, 0))

    #appliquer l'image du poulet
    screen.blit(game.player.image,game.player.rect)

    #recupérer les monstres du jeu
    for monster in game.all_monster:
        monster.update()
        monster.forward()
        if monster.rect.x <= 0:
            monster.orientation = "Right"
        if monster.rect.x >= 1000:
            monster.orientation = "Left"

    #appliquer les images du groupe de monstre
    game.all_monster.draw(screen)

    #verifier si le joueur veut aller à droite ou à gauche
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT):
        game.player.move_left()

    #mettre à jour l'écran
    pygame.display.flip()

    #condition de sortie
    for event in pygame.event.get():
        # verification de l' evenement quietter
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()
        #est ce que le joueur appuie sur une touche
        elif event.type == pygame.KEYDOWN:
            #quelle touche est utilisée
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False