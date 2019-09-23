import pygame
import random
import os
from globalVar import *
class Powerup(pygame.sprite.Sprite):
    def __init__(self, effect):
        pygame.sprite.Sprite.__init__(self)
        self.effect = effect
        if self.effect == 1:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/dmg_pow.gif")).convert()
            self.image = pygame.transform.scale(self.image, (20, 20))
        elif self.effect == 2:
            self.image = pygame.surface.Surface((20, 20))
            self.image.fill((0,0,255))
        elif self.effect == 3:
            self.image = pygame.surface.Surface((20, 20))
            self.image.fill((0,0,0))
        elif self.effect == 4:
            self.image = pygame.surface.Surface((20, 20))
            self.image.fill((20,255,255))
        elif self.effect == 5:
            self.image = pygame.surface.Surface((20, 20))
            self.image.fill((255,0,255))
        self.rect = self.image.get_rect()
        self.rect.y = random.randrange((HEIGHT/2)-50,(HEIGHT/2)+50)
        self.rect.centerx = -50
        self.lastTime = pygame.time.get_ticks()
        self.deathDelay = 10000
        ALL_SPRITES.add(self)
        POWERUPS.add(self)
    def update(self):
        self.rect.x += 3
        if self.rect.x > WIDTH:
            self.kill()
