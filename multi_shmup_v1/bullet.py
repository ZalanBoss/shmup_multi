import pygame
import os
import random
from globalVar import *
#SETS UP THE MOB OBJECT
class Bullet(pygame.sprite.Sprite):
    def __init__(self, posX, posY, _id):
        pygame.sprite.Sprite.__init__(self)
        #MOB VARIABLES
        self.x_size = 10
        self.y_size = 20
        self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/sh.png"))
        self.image = pygame.transform.scale(self.image, (self.x_size, self.y_size))
        self.rect = self.image.get_rect()
        self.rect.y = posY
        self.rect.x = posX
        self.velocity = 10
        self.id = _id
        #ADDS THE OBJECT TO THE 'ALL_SPRITES' PYGAME GROUP
        ALL_SPRITES.add(self)
        #ADDS THE OBJECT TO THE 'BULLET' PYGAME GROUP
    def update(self):
        #MOVEMENT
        self.rect.y -= self.velocity * self.id
        if self.rect.y < 0 or self.rect.y > HEIGHT:
            self.kill()