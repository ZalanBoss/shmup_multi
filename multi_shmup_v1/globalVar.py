import pygame
import os

WIDTH = 600
HEIGHT = 420
FONT_ARIAL = pygame.font.match_font('arial')
RUNNING = True
ALL_SPRITES = pygame.sprite.Group()
MENU_SPRITES = pygame.sprite.Group()
BULLETS_TOP = pygame.sprite.Group()
BULLETS_BOTTOM = pygame.sprite.Group()
PLAYER_BOTTOM = pygame.sprite.Group()
PLAYER_TOP = pygame.sprite.Group()
WALL_BOTTOM = pygame.sprite.Group()
POWERUPS = pygame.sprite.Group()
WALL_TOP = pygame.sprite.Group()
GAME_FOLDER = os.path.dirname(__file__)