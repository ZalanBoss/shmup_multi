import pygame
import random
import os
from globalVar import *
class Powerup(pygame.sprite.Sprite):
    def __init__(self, effect):
        pygame.sprite.Sprite.__init__(self)
        self.effect = effect
        if self.effect == 1:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/dmg_pow.png"))
            self.image = pygame.transform.scale(self.image, (20, 20))
        elif self.effect == 2:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/shoot_spd.png"))
            self.image = pygame.transform.scale(self.image, (20, 20))
        elif self.effect == 3:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/speed_pow.png"))
            self.image = pygame.transform.scale(self.image, (20, 20))
        elif self.effect == 4:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/wall_pow.png"))
            self.image = pygame.transform.scale(self.image, (20, 20))
        elif self.effect == 5:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/hp.png"))
            self.image = pygame.transform.scale(self.image, (20, 20))
        elif self.effect == 6:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/ss.png"))
            self.image = pygame.transform.scale(self.image, (20, 20))
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
