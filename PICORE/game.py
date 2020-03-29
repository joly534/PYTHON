import pygame
from player import Player
from monster import Monster

class Game:

    def __init__(self):
        #générer le joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #groupe de monstre
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_monster()

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monster.add(monster)

    def check_collision(self, sprite, group):
        pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)