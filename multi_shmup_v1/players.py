import pygame
import os
from globalVar import *
from bullet import *
from wall import *
class Players(pygame.sprite.Sprite):
    def __init__(self, posX, posY, _id):
        pygame.sprite.Sprite.__init__(self)
        self.id = _id
        self.shoot_stage = 0
        self.invincible = False
        self.hp = 100
        self.walls = 3
        self.xSize = 45
        self.ySize = 25
        self.image = pygame.image.load(os.path.join(GAME_FOLDER, "./assets/player.png"))
        self.image = pygame.transform.scale(self.image, (self.xSize, self.ySize))
        self.rect = self.image.get_rect()
        self.shoot_snd = pygame.mixer.Sound(os.path.join(GAME_FOLDER, "./assets/shoot.wav"))
        self.rect.x = posX 
        self.rect.y = posY
        self.shoot_delay = 1500
        self.wall_delay = 1600
        self.last_shot = pygame.time.get_ticks()
        self.last_pow = pygame.time.get_ticks()
        self.pow_delay = 21800
        self.last_wall = pygame.time.get_ticks()
        self.damage = 1
        self.speed = 0
        self.velocity = 4
        ALL_SPRITES.add(self)
    def update(self):
        if self.invincible == True:
            self.hp = 100
        self.speed = 0
        if self.shoot_delay <= 120:
            self.shoot_delay = 0 
        if self.hp <= 0:
            self.hp = 0
        if self.hp > 100:
            self.hp = 100 
        #KEYPRESS
        keystate = pygame.key.get_pressed()
        #KEYCHECK AND CHECKS IF IT COLLIDES WITH THE SIDE
        if self.id == 1:
            if keystate[pygame.K_a] and self.rect.x >= 0:
                self.speed -= self.velocity
            if keystate[pygame.K_d] and self.rect.x + self.xSize < WIDTH:
                self.speed += self.velocity
            if keystate[pygame.K_w]:
                self.shoot(1)
            if keystate[pygame.K_s]:
                self.placeWall(1)
        else:
            if keystate[pygame.K_LEFT] and self.rect.x >= 0:
                self.speed -= self.velocity
            if keystate[pygame.K_RIGHT] and self.rect.x + self.xSize < WIDTH:
                self.speed += self.velocity
            if keystate[pygame.K_DOWN]:
                self.shoot(-1)
            if keystate[pygame.K_UP]:
                self.placeWall(2)
        #MOVEMENT
        self.rect.x += self.speed
    def shoot(self, _id):
        self.now = pygame.time.get_ticks()
        if self.id == 1:
            if self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 0:
                self.last_shot = self.now
                x = Bullet(self.rect.x + (self.xSize / 2), self.rect.y - (self.ySize / 2), _id)
                BULLETS_BOTTOM.add(x)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 1:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y - (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y - (self.ySize / 2), _id)
                BULLETS_BOTTOM.add(x, x1)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 2:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y - (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y - (self.ySize / 2), _id)
                x2 = Bullet(self.rect.x + (self.xSize/2), self.rect.y - (self.ySize / 2), _id)
                BULLETS_BOTTOM.add(x, x1, x2)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 3:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y - (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y - (self.ySize / 2), _id)
                x2 = Bullet(self.rect.x + (self.xSize/2), self.rect.y - (self.ySize / 2), _id)
                x3 = Bullet(self.rect.x + (self.xSize/2), self.rect.y - (self.ySize+self.ySize), _id)
                BULLETS_BOTTOM.add(x, x1, x2, x3)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage >= 4:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y - (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y - (self.ySize / 2), _id)
                x2 = Bullet(self.rect.x + (self.xSize/2), self.rect.y - (self.ySize / 2), _id)
                x3 = Bullet(self.rect.x, self.rect.y - (self.ySize+self.ySize), _id)
                x4 = Bullet(self.rect.x + self.xSize, self.rect.y - (self.ySize+self.ySize), _id)
                BULLETS_BOTTOM.add(x, x1, x2, x3, x4)
                self.shoot_snd.play()
        else:
            if self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 0:
                self.last_shot = self.now
                x = Bullet(self.rect.x + (self.xSize / 2), self.rect.y + (self.ySize / 2), _id)
                BULLETS_TOP.add(x)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 1:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y + (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y + (self.ySize / 2), _id)
                BULLETS_TOP.add(x, x1)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 2:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y + (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y + (self.ySize / 2), _id)
                x2 = Bullet(self.rect.x + (self.xSize/2), self.rect.y + (self.ySize / 2), _id)
                BULLETS_TOP.add(x, x1, x2)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage == 3:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y - (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y - (self.ySize / 2), _id)
                x2 = Bullet(self.rect.x + (self.xSize/2), self.rect.y - (self.ySize / 2), _id)
                x3 = Bullet(self.rect.x + (self.xSize/2), self.rect.y + (self.ySize+10), _id)
                BULLETS_TOP.add(x, x1, x2, x3)
                self.shoot_snd.play()
            elif self.now - self.last_shot > self.shoot_delay and self.shoot_stage >= 4:
                self.last_shot = self.now
                x = Bullet(self.rect.x, self.rect.y - (self.ySize / 2), _id)
                x1 = Bullet(self.rect.x + self.xSize, self.rect.y - (self.ySize / 2), _id)
                x2 = Bullet(self.rect.x + (self.xSize/2), self.rect.y - (self.ySize / 2), _id)
                x3 = Bullet(self.rect.x, self.rect.y + (self.ySize+10), _id)
                x4 = Bullet(self.rect.x + self.xSize, self.rect.y + (self.ySize+10), _id)
                BULLETS_TOP.add(x, x1, x2, x3, x4)
                self.shoot_snd.play()
    def placeWall(self, _id):
        self.now2 = pygame.time.get_ticks()
        if _id == 2 and self.walls > 0 and self.now2 - self.last_wall > self.wall_delay:
            self.last_wall = self.now2
            x = Wall(self.rect.y + 60, self.rect.centerx)
            WALL_TOP.add(x)
            self.walls -= 1
        elif _id == 1 and self.walls > 0 and self.now2 - self.last_wall > self.wall_delay:
            self.last_wall = self.now2
            x = Wall(self.rect.y - 60, self.rect.centerx)
            WALL_BOTTOM.add(x)
            self.walls -= 1
    def shoot_stage_up(self):
        self.shoot_stage += 1
        print("shoot-----s",self.shoot_stage)
        self.now3 = pygame.time.get_ticks()
        #if self.shoot_stage > 0 and self.now3 - self.last_pow > self.pow_delay:
        #    self.last_pow = self.now3
        #    self.shoot_stage -= 1
        #    print("shot____s", self.shoot_stage)
        