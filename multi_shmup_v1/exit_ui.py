import pygame
import os
from globalVar import *
class ExitUi(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/exit.png"))
        self.width = 200
        self.height = 100
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH/2
        self.rect.centery = HEIGHT/2 + self.width/2
        MENU_SPRITES.add(self)
    def update(self):
        pass
    def hasBeenPressed(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.width:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + self.height:
                return True
            
        return False