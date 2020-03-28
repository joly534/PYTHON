import pygame

#creation de la classe poulet
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.speed = 5
        self.attack = 10
        self.image = pygame.image.load("image/chicken1.png")
        self.rect = self.image.get_rect()
        self.rect.y = 4
        self.rect.x= 500

    def move_right(self):
        if self.rect.x < 1130 :
            self.rect.x += self.speed
        else:
            self.rect.x += 0


    def move_left(self):
        if self.rect.x > 0 :
            self.rect.x -= self.speed
        else:
            self.rect.x += 0