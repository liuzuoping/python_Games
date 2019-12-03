import pygame
import random

class Food(pygame.sprite.Sprite):
    def __init__(self):
        
        self.food_boom    = pygame.image.load(r"..\image\food_boom.png").convert_alpha()
        self.food_clock   = pygame.image.load(r"..\image\food_clock.png").convert_alpha()
        self.food_gun     = pygame.image.load(r"..\image\food_gun.png").convert_alpha()
        self.food_iron    = pygame.image.load(r"..\image\food_iron.png").convert_alpha()
        self.food_protect = pygame.image.load(r"..\image\food_protect.png").convert_alpha()
        self.food_star    = pygame.image.load(r"..\image\food_star.png").convert_alpha()
        self.food_tank    = pygame.image.load(r"..\image\food_tank.png").convert_alpha()
        self.kind = random.choice([1, 2, 3, 4, 5, 6, 7])
        if self.kind == 1:
            self.image = self.food_boom
        elif self.kind == 2:
            self.image = self.food_clock
        elif self.kind == 3:
            self.image = self.food_gun
        elif self.kind == 4:
            self.image = self.food_iron
        elif self.kind == 5:
            self.image = self.food_protect
        elif self.kind == 6:
            self.image = self.food_star
        elif self.kind == 7:
            self.image = self.food_tank
            
        self.rect = self.image.get_rect()
        self.rect.left = self.rect.top = random.randint(100, 500)
        
        self.life = False
        
    def change(self):
        self.kind = random.choice([1, 2, 3, 4, 5, 6, 7])
        if self.kind == 1:
            self.image = self.food_boom
        elif self.kind == 2:
            self.image = self.food_clock
        elif self.kind == 3:
            self.image = self.food_gun
        elif self.kind == 4:
            self.image = self.food_iron
        elif self.kind == 5:
            self.image = self.food_protect
        elif self.kind == 6:
            self.image = self.food_star
        elif self.kind == 7:
            self.image = self.food_tank
            
        self.rect.left = self.rect.top = random.randint(100, 500)
        self.life = True
        
            