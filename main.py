import math
import random
import pygame
from pygame import mixer
import enemy as enemy_class
import weapon as weapon_class
import waves as wave_class

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((1200, 1000))

# Caption and Icon
pygame.display.set_caption("Posh Invader")
icon = pygame.image.load("pet.png")
pygame.display.set_icon(icon)
test_count = 0
start_ticks=pygame.time.get_ticks()
#Player-----------------------------------------------------------------------------------------Player
player_image = pygame.image.load("cat.png")
player_image2 = pygame.image.load("cat2.png") 
global direction 
direction = True
playerX = 580
playerY = 600
X_deltaval_speed = 1.2
Y_deltaval_speed = 1.2
Y_wrap = False
#left right movement
moveLR = False
mL = False
mR = False
#up down movement
moveUD = False
mU = False
mD = False

def player():
    screen.blit(player_image, (int(playerX), int(playerY)))
def player2():
    screen.blit(player_image2, (int(playerX), int(playerY)))

#Player_Weapons-------------------------------------------------------------------------------Player_Weapons
global bullets
bullets = []

def fire_bullet(i):
    bullets[i].bullet_state = "fire"
    screen.blit(bullets[i].bullet_image, (int(bullets[i].bulletX), int(bullets[i].bulletY)))

laser = weapon_class.laser()
def fire_laser():
    screen.blit(laser.bullet_image, (int(playerX - 50), int(playerY - 890)))

current_weapon_count = 0
#Enemy-----------------------------------------------------------------------------------------Enemy
enemy_spawns = wave_class.waveinfo()
wave1 = enemy_spawns.wave1
enemies = []

def enemy(x, y, i):
    if enemies[i].dead == False:
        screen.blit(enemies[i].enemy_image, (int(x),int(y)))

#Functions--------------------------------------------------------------------------------------Functions
font = pygame.font.Font('freesansbold.ttf', 32)
over_font = pygame.font.Font('freesansbold.ttf', 64)
under_font = pygame.font.Font('freesansbold.ttf', 34)

lives_image = pygame.image.load("lives.png")
speed_image = pygame.image.load("cats.png")
speed_image2 = pygame.image.load("cat_empty.png")
player_score = 0
num_lives = 3
speed_boosts = 3
lives_timer = True

def title():
    title = over_font.render("Space Jammers", True, (255,255,255))
    title2 = under_font.render("Press Space to begin", True, (255,255,255))
    screen.blit(title, (350, 400))
    screen.blit(title2, (430, 480))

def score():
    scoreboard = font.render("Score: " + str(player_score), True, (255,255,255))
    screen.blit(scoreboard, (10, 10))

def game_over():
    over_banner = over_font.render("Meowzers! It's over!", True, (255,255,255))
    screen.blit(over_banner, (350, 400))
    start_game = False

def lives(num_lives):
    livesX = 110
    livesY = 50
    lives_text = font.render("Lives:", True, (255,255,255))
    screen.blit(lives_text, (10,50))
    for i in range(num_lives):
        screen.blit(lives_image,(livesX, livesY))
        livesX += 30

# def speedy(speed_boosts):
#     speedyX = 110
#     speedyY = 90
#     speed_text = font.render("Fast:", True, (255,255,255))
#     screen.blit(speed_text, (10, 90))
#     for i in range(speed_boosts):
#         screen.blit(speed_image, (int(speedyX), int(speedyY)))
#         speedyX += 30

def weapon_equip(wep):
    wepX = 110
    wepY = 90
    wep_text = font.render("Wep: " + wep, True, (255, 255, 255))
    screen.blit(wep_text, (10, 90))
    

def collision_player(enemyX, enemyY, playerX, playerY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 30:
        return True
    else:
        return False

def collision(enemyX, enemyY, i):
    distance = math.sqrt(math.pow(enemyX - bullets[i].bulletX, 2) + (math.pow(enemyY - bullets[i].bulletY, 2)))
    if distance < 30:
        return True
    else:
        return False

def laser_collision(enemyX, enemyY):
    distance = math.sqrt(math.pow(enemyX - playerX, 2))
    distance2 = math.sqrt(math.pow(enemyX - playerX, 2) + (math.pow(enemyY - playerY, 2)))
    if distance < 30 or distance2 < 50:
        return True
    else:
        return False


#####################################################################################################################
############## Game Loop ######################## Game Loop ########################## Game Loop ####################
#####################################################################################################################
running = True
defeat = False
start_game = False
while running:
    if start_game:
        seconds = (pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    # Keystroke listener----------------------------------------------------------------------------Keystroke listener
            
            if event.type == pygame.KEYDOWN:
                # Player movement
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    moveLR = True
                    mL = True
                    X_deltaval = -X_deltaval_speed
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:    
                    moveLR = True
                    mR = True
                    X_deltaval = X_deltaval_speed
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    moveUD = True
                    mU = True
                    Y_deltaval = -Y_deltaval_speed
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    moveUD = True
                    mD = True
                    Y_deltaval = Y_deltaval_speed
                # Player Weapons
                if event.key == pygame.K_m:
                    if speed_boosts > 0:
                        speed_boosts -= 1
                        X_deltaval_speed += 1
                        Y_deltaval_speed += 1
                if event.key == pygame.K_r:
                    current_weapon_count += 1
                    current_weapon_count = current_weapon_count%3
                if event.key == pygame.K_SPACE:
                    if not bullets:
                        if current_weapon_count == 0:
                            bullets.append(weapon_class.basic_bullet(bulletX = playerX, bulletY = playerY))
                            bullet_index = len(bullets) - 1
                            fire_bullet(bullet_index)
                        elif current_weapon_count == 1:
                            bullets.append(weapon_class.basic_bullet(bulletX = playerX + 8, bulletY = playerY))
                            bullet_index = len(bullets) - 1
                            fire_bullet(bullet_index)
                            bullets.append(weapon_class.basic_bullet(bulletX = playerX - 8, bulletY = playerY))
                            bullet_index = len(bullets) - 1
                            fire_bullet(bullet_index)
                        elif current_weapon_count == 2:
                            bullets.append(weapon_class.basic_bullet(bulletX = playerX , bulletY = playerY))
                            bullet_index = len(bullets) - 1
                            fire_bullet(bullet_index)
                            bullets.append(weapon_class.basic_bullet(bulletX = playerX - 12, bulletY = playerY))
                            bullet_index = len(bullets) - 1
                            fire_bullet(bullet_index)
                            bullets.append(weapon_class.basic_bullet(bulletX = playerX + 12, bulletY = playerY))
                            bullet_index = len(bullets) - 1
                            fire_bullet(bullet_index)
                if event.key == pygame.K_v:
                    laser.bullet_state = "fire"

                #DEBUG
                # if event.key == pygame.K_w:
                #     Y_wrap = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    mL = False
                    if mR:
                        X_deltaval = X_deltaval_speed
                    else:
                        moveLR = False
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:    
                    mR = False
                    if mL:
                        X_deltaval = -X_deltaval_speed
                    else:
                        moveLR = False
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    mU = False
                    if mD:
                        Y_deltaval = Y_deltaval_speed
                    else:
                        moveUD = False
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    mD = False
                    if mU:
                        Y_deltaval = -Y_deltaval_speed
                    else:
                        moveUD = False
                if event.key == pygame.K_v:
                    laser.bullet_state = "ready"

        # screen.blit(background,(0,0))
        if num_lives <= 0:
            game_over()
        else:
            screen.fill((12,0,0))

    #Player movement processing---------------------------------------------------------------------Player movement processing
        if moveLR:
            playerX_change = X_deltaval
            if X_deltaval > 0:
                direction = True
            elif X_deltaval <= 0:
                direction = False
        else:
            playerX_change = 0

        if moveUD:
            playerY_change = Y_deltaval
        else:
            playerY_change = 0

        playerX += playerX_change #Player XY location
        playerX = playerX%1200 #Player X wraparound

        playerY += playerY_change
        if Y_wrap == False:
            if playerY > 930:
                playerY = 930
            elif playerY < 0:
                playerY = 0
        else:
            playerY = playerY%1000 #Y wraparound

        if current_weapon_count == 0:
            equipped = "pea shooter"
        elif current_weapon_count == 1:
            equipped = "pea2 shooter"
        elif current_weapon_count == 2:
            equipped = "pea3 shooter"
        elif current_weapon_count == 3:
            equipped = "LASER"

    #Enemy movement processing------------------------------------------------------------------------Enemy movement processing
        for i in range(len(enemies)):
            if enemies[i].move == 1:
                enemies[i].X += enemies[i].X_deltaval_speed
                if enemies[i].X <= 0 or enemies[i].X >= 1150:
                    enemies[i].X_deltaval_speed = -enemies[i].X_deltaval_speed
                    enemies[i].Y += enemies[i].Y_deltaval_speed #Moves enemy down a row
                    if enemies[i].Y > 1000:
                        enemies[i].dead = True
            elif enemies[i].move == 2:
                enemies[i].X -= enemies[i].X_deltaval_speed
                if enemies[i].X <= 0 or enemies[i].X >= 1150:
                    enemies[i].X_deltaval_speed = -enemies[i].X_deltaval_speed
                    enemies[i].Y += enemies[i].Y_deltaval_speed #Moves enemy down a row
                    if enemies[i].Y > 1000:
                        enemies[i].dead = True
            enemy(enemies[i].X, enemies[i].Y, i)

            # If bullet hits a baddie
            if bullets:
                for j in range(len(bullets)):
                    if collision(enemies[i].X, enemies[i].Y, j):
                        explosionSound = mixer.Sound("explosion.wav")
                        explosionSound.play()
                        bullets[j].bullet_state = "ready"
                        bullets[j].bulletX = -999
                        bullets[j].bulletY = -999
                        enemies[i].hp -= bullets[j].damage 
                        if enemies[i].hp <= 0:
                            player_score += enemies[i].score
                            enemies[i].dead = True

            # LASERS
            if laser.bullet_state == "fire":
                if laser_collision(enemies[i].X, enemies[i].Y):
                    explosionSound = mixer.Sound("explosion.wav")
                    explosionSound.play()
                    enemies[i].hp -= laser.damage
                    if enemies[i].hp <= 0:
                        player_score += enemies[i].score
                        enemies[i].dead = True

            # If player hits a baddie
            if collision_player(enemies[i].X, enemies[i].Y, playerX, playerY):
                num_lives -= 1
                player_score += enemies[i].score
                enemies[i].dead = True

        if bullets:
             for j in range(len(bullets)):
                fire_bullet(j)
                bullets[j].bulletY -= bullets[j].bullet_Y_deltaval_speed
                if bullets[j].bulletY < 0:
                    bullets[j].bullet_state = "ready"

        dead_enemies = []
        for i in range(len(enemies)):
            if enemies[i].dead == True:
                dead_enemies.append(i)
        
        for i in range(len(dead_enemies)):
            try:
                enemies.pop(dead_enemies[i])
            except:
                pass
        if not enemies:
            # print("WAVEDONE")
            pass

        dead_bullets = []
        for i in range(len(bullets)):
            if bullets[i].bullet_state == "ready":
                dead_bullets.append(i)

        for i in range(len(dead_bullets)):
            try:
                bullets.pop(dead_bullets[i])
            except:
                pass



        waveinfo = wave1[0]
        #Generate enemies
        if not enemies:
            for i in range(len(waveinfo)):
                #enemy id
                if waveinfo[i][0] == 1:
                    enemies.append(enemy_class.basic_enemy(waveinfo[i][1][0], waveinfo[i][1][1], waveinfo[i][2]))
                    
                
        if laser.bullet_state == "fire":
            fire_laser()        
        score()
        lives(num_lives)
        weapon_equip(equipped)
        if direction == False:
            player2() #renders player model
        else:
            player()
        pygame.display.update()


#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen
#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen
    
    else: #Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen#Home screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_game = True
        screen.fill((0,0,0))
        title()
        player()
        pygame.display.update()

    