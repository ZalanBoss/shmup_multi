import pygame
from globalVar import *
class HpBar(pygame.sprite.Sprite):
    def __init__(self, player, posY):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.surface.Surface((self.player.hp * 2, 10))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect()
        self.rect.y = posY
        self.rect.centerx = WIDTH/2
        self.lastHp = self.player.hp
        ALL_SPRITES.add(self)
    def update(self):
        if self.lastHp != self.player.hp and 0 < self.player.hp:
            self.image = pygame.transform.scale(self.image, (self.player.hp * 2, 10))
            self.lastHp = self.player.hp
        elif self.player.hp <= 0:
            self.kill()
    def death(self):
        pass