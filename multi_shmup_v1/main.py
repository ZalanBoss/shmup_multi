import pygame
import random
from globalVar import *
from players import *
from hpBar import *
from powerup import *
class mainState:
    def __init__(self):
        self.fps = 30
        self.tittle = "Shmup"
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        self.who_wins = 0
        self.clock = pygame.time.Clock()
        self.pow_snds = []
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(self.tittle)
        self.hit_snd = pygame.mixer.Sound(os.path.join(GAME_FOLDER, "./assets/hit.wav"))
        self.Shieldhit_snd = pygame.mixer.Sound(os.path.join(GAME_FOLDER, "./assets/shield_hit.wav"))
        self.Bullethit_snd = pygame.mixer.Sound(os.path.join(GAME_FOLDER, "./assets/bullet_hit.wav"))
        pygame.mixer.music.load(os.path.join(GAME_FOLDER, "./assets/game_music.wav"))
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)
        for snd in ["./assets/Powerup_1.wav", "./assets/Powerup_2.wav", "./assets/Powerup_3.wav", "./assets/Powerup_4.wav", "./assets/Powerup_5.wav"]:
            self.pow_snds.append(pygame.mixer.Sound(os.path.join(GAME_FOLDER, snd)))
        
    def draw_text(self, surf,text,size,x,y,anti_alias,color):
        font = pygame.font.Font(FONT_ARIAL, size)
        text_surf = font.render(text, anti_alias, color)
        text_rect = text_surf.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surf, text_rect)
    def SPAWNPOWERUP(self, chance, effect):
        rand = random.randrange(1, chance)
        rand_effect = effect
        if rand == 50:
            Powerup(rand_effect)
    def collide(self):
        hits = pygame.sprite.groupcollide(BULLETS_TOP, BULLETS_BOTTOM, True, True)
        if hits:
            for hit in hits:
                self.Bullethit_snd.play()
        hits = pygame.sprite.groupcollide(PLAYER_BOTTOM, BULLETS_TOP, False, True)
        if hits:
            for hit in hits:
                hit.hp -= player_top.damage
                self.hit_snd.play()
        hits = pygame.sprite.groupcollide(PLAYER_TOP, BULLETS_BOTTOM, False, True)
        if hits:
            for hit in hits:
                hit.hp -= player_bottom.damage
                self.hit_snd.play()
        hits = pygame.sprite.groupcollide(BULLETS_BOTTOM, WALL_TOP, True, False)
        if hits:
            for hit in hits:
                self.Shieldhit_snd.play()
        hits = pygame.sprite.groupcollide(BULLETS_TOP, WALL_BOTTOM, True, False)
        if hits:
            for hit in hits:
                self.Shieldhit_snd.play()
        hits = pygame.sprite.groupcollide(BULLETS_TOP, WALL_TOP, False, False)
        if hits:
            for hit in hits:
                hit.velocity = 1
        hits = pygame.sprite.groupcollide(BULLETS_BOTTOM, WALL_BOTTOM, False, False)
        if hits:
            for hit in hits:
                hit.velocity = 1
        hits = pygame.sprite.groupcollide(POWERUPS, BULLETS_BOTTOM, True, True)
        if hits:
            for hit in hits:
                random.choice(self.pow_snds).play()
                if hit.effect == 1:
                    player_bottom.damage += 1
                elif hit.effect == 2:
                    player_bottom.shoot_delay -= 70
                elif hit.effect == 3:
                    player_bottom.velocity += 0.5
                elif hit.effect == 4:
                    player_bottom.walls += 1
                elif hit.effect == 5:
                    player_bottom.hp += int(player_top.hp/10)
                    if player_bottom.hp < 20:
                        player_bottom.hp += int(player_top.hp/2)
                elif hit.effect == 6:
                    player_bottom.shoot_stage_up()
        hits = pygame.sprite.groupcollide(POWERUPS, BULLETS_TOP, True, True)
        if hits:
            for hit in hits:
                random.choice(self.pow_snds).play()
                if hit.effect == 1:
                    player_top.damage += 1
                elif hit.effect == 2:
                    player_top.shoot_delay -= 70
                elif hit.effect == 3:
                    player_top.velocity += 0.5
                elif hit.effect == 4:
                    player_top.walls += 1
                elif hit.effect == 5:
                    player_top.hp += int(player_bottom.hp/10)
                    if player_top.hp < 20:
                        player_top.hp += int(player_bottom.hp/2)
                elif hit.effect == 6:
                    player_top.shoot_stage_up()
                    
mainGame = mainState()
player_bottom = Players(
    WIDTH/2,
    HEIGHT - 50,
    1,
)
PLAYER_BOTTOM.add(player_bottom)
player_top = Players(
    WIDTH/2,
    0 + 50,
    2,
)
PLAYER_TOP.add(player_top)
hpbarBottom = HpBar(player_bottom, HEIGHT-20)
hpbarTop = HpBar(player_top, 25)

while RUNNING:
    mainGame.clock.tick(mainGame.fps)
    mainGame.collide()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
    if player_top.hp <= 0:
        player_top.kill()
        mainGame.who_wins = 2
        player_bottom.invincible = True
    elif player_bottom.hp <= 0:
        player_bottom.kill()
        mainGame.who_wins = 1
        player_top.invincible = True
    
    mainGame.SPAWNPOWERUP(400, 1)
    mainGame.SPAWNPOWERUP(600, 2)
    mainGame.SPAWNPOWERUP(700, 3)
    mainGame.SPAWNPOWERUP(200, 4)
    mainGame.SPAWNPOWERUP(1000, 5)
    mainGame.SPAWNPOWERUP(800, 6)
    ALL_SPRITES.update()
    mainGame.screen.fill((10,100,130))
    ALL_SPRITES.draw(mainGame.screen)
    mainGame.draw_text(mainGame.screen,"Walls: ",14,25,25,True,(255,255,255))
    mainGame.draw_text(mainGame.screen,str(player_top.walls),14,50,25,True,(0,255,0))
    mainGame.draw_text(mainGame.screen,"Damage: ",14,100,25,True,(255,255,255))
    mainGame.draw_text(mainGame.screen,str(player_top.damage),14,140,25,True,(255,165,0))
    mainGame.draw_text(mainGame.screen,"HP: ",20,180,20,True,(0,150,0))
    mainGame.draw_text(mainGame.screen,"shoot delay: ",14,WIDTH-100,25,True,(0,150,0))
    mainGame.draw_text(mainGame.screen,str(player_top.shoot_delay),14,WIDTH-40,25,True,(0,255,255))


    if mainGame.who_wins == 1:
        mainGame.draw_text(mainGame.screen,"PLAYER TOP WINS",44,WIDTH/2,HEIGHT/2,True,(255,0,0))
    elif mainGame.who_wins == 2:
        mainGame.draw_text(mainGame.screen,"PLAYER BOTTOM WINS",44,WIDTH/2,HEIGHT/2,True,(255,0,0))
    mainGame.draw_text(mainGame.screen,"Walls: ",14,25,HEIGHT-25,True,(255,255,255))
    mainGame.draw_text(mainGame.screen,str(player_bottom.walls),14,50,HEIGHT-25,True,(0,255,0))
    mainGame.draw_text(mainGame.screen,"Damage: ",14,100,HEIGHT-25,True,(255,255,255))
    mainGame.draw_text(mainGame.screen,str(player_bottom.damage),14,140,HEIGHT-25,True,(255,165,0))
    mainGame.draw_text(mainGame.screen,"HP: ",20,180,HEIGHT-25,True,(0,150,0))
    mainGame.draw_text(mainGame.screen,"shoot delay: ",14,WIDTH-100,HEIGHT-25,True,(0,150,0))
    mainGame.draw_text(mainGame.screen,str(player_bottom.shoot_delay),14,WIDTH-40,HEIGHT-25,True,(0,255,255))

    
    pygame.display.flip()

pygame.quit()