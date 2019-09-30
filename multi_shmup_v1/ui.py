import pygame
import os
from globalVar import *
class Button(pygame.sprite.Sprite):
    def __init__(self, image, width, height, x, y,group = MENU_SPRITES):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        group.add(self)
    def update(self):
        pass
    def isPressed(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.rect.x and pos[0] < self.rect.x + self.width:
            if pos[1] > self.rect.y and pos[1] < self.rect.y + self.height:
                return True
            
        return False
    def death(self):
        pass
class Text:
    def __init__(self,surf,text,x,y,color, font = FONT_ARIAL, size = 14,anti_alias = True):
        self.surf = surf
        self.text = text
        self.size = size
        self.x = x
        self.y = y
        self.anti_alias = anti_alias
        self.color = color
        self.font = font
    def draw(self):
        font = pygame.font.Font(self.font, self.size)
        text_surf = font.render(self.text, self.anti_alias, self.color)
        text_rect = text_surf.get_rect()
        text_rect.midtop = (self.x, self.y)
        self.surf.blit(text_surf, text_rect)