import pygame
import random
from globalVar import *
from players import *
from hpBar import *
from powerup import *
from ui import *
class mainState:
    def __init__(self):
        self.mainMenu = True
        self.controls_ = False
        self.game_run = False
        self.fps = 30
        self.game_end = False
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
start_ui = Button(pygame.image.load(os.path.join(GAME_FOLDER, "./assets/start.png")), 200, 100, WIDTH/2, HEIGHT/2)
exit_ui = Button(pygame.image.load(os.path.join(GAME_FOLDER, "./assets/exit.png")), 200, 100,
                                     WIDTH/2, HEIGHT/2 + 200/2)
menu_ui = Button(pygame.image.load(os.path.join(GAME_FOLDER, "./assets/menu.png")), 20, 20,
                                     WIDTH+20, 40, group=ALL_SPRITES)
menu_ui_cont = Button(pygame.image.load(os.path.join(GAME_FOLDER, "./assets/menu.png")), 20, 20,
                                     WIDTH+20, 40, group=CONTROLS_MENU_SPRITES)
controlls_ui = Button(pygame.image.load(os.path.join(GAME_FOLDER, "./assets/controls.png")), 80, 80,
                                     WIDTH-40, 70)
while RUNNING:
    if mainGame.game_run == True:
        mainGame.clock.tick(mainGame.fps)
        mainGame.collide()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_ui.isPressed(pos) == True:
                        mainGame.mainMenu = True
                        mainGame.game_run = False
                        mainGame.who_wins = 0
                        for a in ALL_SPRITES:
                            a.death()
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
                        hpbarBottom.kill()
                        hpbarTop.kill()
                        hpbarBottom = HpBar(player_bottom, HEIGHT-20)
                        hpbarTop = HpBar(player_top, 25)
                        pygame.mixer.music.set_volume(0)
                        mainGame.game_end = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if mainGame.game_end == True:
                        mainGame.mainMenu = True
                        mainGame.game_run = False
                        mainGame.who_wins = 0
                        for a in ALL_SPRITES:
                            a.death()
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
                        hpbarBottom.kill()
                        hpbarTop.kill()
                        hpbarBottom = HpBar(player_bottom, HEIGHT-20)
                        hpbarTop = HpBar(player_top, 25)
                        pygame.mixer.music.set_volume(0)
                        mainGame.game_end = False
            if event.type == pygame.QUIT:
                RUNNING = False
        if player_top.hp <= 0:
            player_top.kill()
            mainGame.who_wins = 2
            player_bottom.invincible = True
            mainGame.game_end = True
        elif player_bottom.hp <= 0:
            player_bottom.kill()
            mainGame.who_wins = 1
            player_top.invincible = True
            mainGame.game_end = True
        
        mainGame.SPAWNPOWERUP(800, 1)
        mainGame.SPAWNPOWERUP(1000, 2)
        mainGame.SPAWNPOWERUP(1100, 3)
        mainGame.SPAWNPOWERUP(600, 4)
        mainGame.SPAWNPOWERUP(1400, 5)
        mainGame.SPAWNPOWERUP(1200, 6)
        ALL_SPRITES.update()
        mainGame.screen.fill((10,100,130))
        ALL_SPRITES.draw(mainGame.screen)
        Text(mainGame.screen,"Walls: ",25,25,(255,255,255)).draw()
        Text(mainGame.screen,str(player_top.walls),50,25,(0,255,0)).draw()
        Text(mainGame.screen,"Damage: ",100,25,(255,255,255)).draw()
        Text(mainGame.screen,str(player_top.damage),140,25,(255,165,0)).draw()
        Text(mainGame.screen,"HP: ",180,20,(0,150,0),size=20).draw()
        Text(mainGame.screen,"shoot delay: ",WIDTH-100,25,(0,150,0)).draw()
        Text(mainGame.screen,str(player_top.shoot_delay),WIDTH-40,25,(0,255,255)).draw()

        if mainGame.who_wins == 1:
            Text(mainGame.screen,"PLAYER TOP WINS",WIDTH/2,HEIGHT/2,(255,0,0), size=44).draw()
        elif mainGame.who_wins == 2:
            Text(mainGame.screen,"PLAYER BOTTOM WINS",WIDTH/2,HEIGHT/2,(255,0,0), size=44).draw()
        Text(mainGame.screen,"Walls: ",25,HEIGHT-25,(255,255,255)).draw()
        Text(mainGame.screen,str(player_bottom.walls),50,HEIGHT-25,(0,255,0)).draw()
        Text(mainGame.screen,"Damage: ",100,HEIGHT-25,(255,255,255)).draw()
        Text(mainGame.screen,str(player_bottom.damage),140,HEIGHT-25,(255,165,0)).draw()
        Text(mainGame.screen,"HP: ",180,HEIGHT-25,(0,150,0),size = 20).draw()
        Text(mainGame.screen,"shoot delay: ",WIDTH-100,HEIGHT-25,(0,150,0)).draw()
        Text(mainGame.screen,str(player_bottom.shoot_delay),WIDTH-40,HEIGHT-25,(0,255,255)).draw()
        
        pygame.display.flip()
    elif mainGame.mainMenu == True: 
        mainGame.clock.tick(mainGame.fps)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_ui.isPressed(pos) == True:
                    mainGame.mainMenu = False
                    mainGame.game_run = True
                    pygame.mixer.music.set_volume(0.4)
                    pygame.mixer.music.play(loops=-1)
                elif exit_ui.isPressed(pos) == True:
                    RUNNING = False
                elif controlls_ui.isPressed(pos): 
                    mainGame.mainMenu = False
                    mainGame.game_run = False
                    mainGame.controls_ = True
            if event.type == pygame.QUIT:
                RUNNING = False
        
        MENU_SPRITES.update()
        mainGame.screen.fill((255,114,255))
        MENU_SPRITES.draw(mainGame.screen)

        Text(mainGame.screen, "MULTI SHMUP", WIDTH/2, 20, (25,144,234), size=50).draw()
        pygame.display.flip()
    elif mainGame.controls_:
        mainGame.clock.tick(mainGame.fps)
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if menu_ui_cont.isPressed(pos) == True:
                    mainGame.controls_ = False
                    mainGame.mainMenu = True
            if event.type == pygame.QUIT:
                RUNNING = False
        CONTROLS_MENU_SPRITES.update()
        mainGame.screen.fill((114,114,114))
        CONTROLS_MENU_SPRITES.draw(mainGame.screen)
        Text(mainGame.screen, "MULTI SHMUP", WIDTH/2, 20, (25,144,234), size=50).draw()
        Text(mainGame.screen, "TOP PLAYER MOVE LEFT : L_ARROW", 140, 80, (25,144,234)).draw()
        Text(mainGame.screen, "TOP PLAYER MOVE RIGHT : R_ARROW", 145, 100, (25,144,234)).draw()
        Text(mainGame.screen, "TOP PLAYER SHOOT : DOWN_ARROW", 143, 120, (225,144,234)).draw()
        Text(mainGame.screen, "TOP PLAYER PLACE SHIELD : UP_ARROW", 155, 140, (25,144,234)).draw()

        Text(mainGame.screen, "BOTTOM PLAYER MOVE LEFT : a", 130, 180, (25,144,234)).draw()
        Text(mainGame.screen, "BOTTOM PLAYER MOVE RIGHT : d", 133, 200, (25,144,234)).draw()
        Text(mainGame.screen, "BOTTOM PLAYER SHOOT : w", 115, 220, (225,144,234)).draw() 
        Text(mainGame.screen, "BOTTOM PLAYER PLACE SHIELD : ws", 143, 240, (25,144,234)).draw()
        pygame.display.flip()
        
        
pygame.quit()
quit()