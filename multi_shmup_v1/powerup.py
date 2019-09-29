import pygame
import random
import os
from globalVar import *
class Powerup(pygame.sprite.Sprite):
    def __init__(self, effect):
        pygame.sprite.Sprite.__init__(self)
        self.effect = effect
        self.rand = random.randrange(0,100)
        if self.effect == 1:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/dmg_pow.png"))
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif self.effect == 2:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/shoot_spd.png"))
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif self.effect == 3:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/speed_pow.png"))
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif self.effect == 4:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/wall_pow.png"))
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif self.effect == 5:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/hp.png"))
            self.image = pygame.transform.scale(self.image, (30, 30))
        elif self.effect == 6:
            self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/ss.png"))
            self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = self.image.get_rect()
        if self.rand % 2 == 0:
            self.velocity = 3
            self.rect.centerx = -50
        else:
            self.rect.centerx = WIDTH+50
            self.velocity = -3
        self.rect.y = random.randrange((HEIGHT/2)-50,(HEIGHT/2)+50)
        self.lastTime = pygame.time.get_ticks()
        self.deathDelay = 10000
        ALL_SPRITES.add(self)
        POWERUPS.add(self)
    def update(self):
        self.rect.x += self.velocity
        if self.rect.x > WIDTH and self.rand % 2 == 0:
            self.kill()
        elif self.rect.x < -30 and self.rand % 2 == 1:
            self.kill()
    def death(self):
        self.kill()
