import pygame

brickImage          = r"..\image\brick.png"
ironImage           = r"..\image\iron.png"

class Brick(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(brickImage)
        self.rect = self.image.get_rect()
        
class Iron(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(ironImage)
        self.rect = self.image.get_rect()
        
class Map():
    def __init__(self):
        self.brickGroup = pygame.sprite.Group()
        self.ironGroup  = pygame.sprite.Group()
        
        # 数字代表地图中的位置
        # 画砖块
        X1379 = [2, 3, 6, 7, 18, 19, 22, 23]
        Y1379 = [2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 18, 19, 20, 21, 22, 23]
        X28 = [10, 11, 14, 15]
        Y28 = [2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 17, 18, 19, 20]
        X46 = [4, 5, 6, 7, 18, 19, 20, 21]
        Y46 = [13, 14]
        X5  = [12, 13]
        Y5  = [16, 17]
        X0Y0 = [(11,23),(12,23),(13,23),(14,23),(11,24),(14,24),(11,25),(14,25)]
        for x in X1379:
            for y in Y1379:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X28:
            for y in Y28:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X46:
            for y in Y46:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x in X5:
            for y in Y5:
                self.brick = Brick()
                self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
                self.brickGroup.add(self.brick)
        for x, y in X0Y0:
            self.brick = Brick()
            self.brick.rect.left, self.brick.rect.top = 3 + x * 24, 3 + y * 24
            self.brickGroup.add(self.brick)
        
        # 画石头
        for x, y in [(0,14),(1,14),(12,6),(13,6),(12,7),(13,7),(24,14),(25,14)]:
            self.iron = Iron()
            self.iron.rect.left, self.iron.rect.top = 3 + x * 24, 3 + y * 24
            self.ironGroup.add(self.iron)
            
        