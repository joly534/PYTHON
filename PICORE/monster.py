import pygame

#classe qui gère la notion de monstre
class Monster(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (1).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (2).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (3).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (4).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (5).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (6).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (7).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (8).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (9).png'))
        self.sprites.append(pygame.image.load('image/zombies/male/Walk (10).png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        

        self.game = game
        self.health = 100
        self.max_health = 100          
        self.speed = 0.2 
        self.attack = 5
        self.rect = self.image.get_rect()
        self.rect.x = 900
        self.rect.y = 110
        self.orientation = 'left'

    def update(self):
        self.current_sprite += 0.15
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

    def blit(self):
        if self.orientation == "Right":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Left":
            self.screen.blit(pygame.transform.flip(self.image, False, True), self.rect)


    def forward(self):
        #le déplacement est autorisé seulement hors collicion
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.speed
    