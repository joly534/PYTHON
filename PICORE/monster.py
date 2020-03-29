import pygame

#classe qui gère la notion de monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100          
        self.speed = 0.5  
        self.attack = 5
        self.image = pygame.image.load("image/zombies/zombie.png")
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 110

    def forward(self):
        #le déplacement est autorisé seulement hors collicion
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.speed
    