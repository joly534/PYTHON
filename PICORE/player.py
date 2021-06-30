import pygame


#creation de la classe poulet
class Player(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()

        self.sprites = []
        self.sprites.append(pygame.image.load('image/chicken.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.game = game
        self.health = 100
        self.max_health = 100
        self.speed = 5
        self.attack = 10
        self.image = pygame.image.load("image/chicken1.png")
        self.rect = self.image.get_rect()
        self.rect.y = 15
        self.rect.x= 500

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x -= self.speed


    def move_left(self):
        if self.rect.x > 0 :
            self.rect.x -= self.speed
        else:
            self.rect.x += 0