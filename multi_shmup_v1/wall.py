import pygame
from globalVar import *
class Wall(pygame.sprite.Sprite):
    def __init__(self, posY, posX):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.surface.Surface((75, 10))
        self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.y = posY
        self.rect.centerx = posX
        self.lastTime = pygame.time.get_ticks()
        self.deathDelay = 30000
        ALL_SPRITES.add(self)
    def update(self):
        self.now = pygame.time.get_ticks()
        if self.now - self.lastTime > self.deathDelay:
            self.last_shot = self.now
            self.kill()
    def death(self):
        self.kill()
     