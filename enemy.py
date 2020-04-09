import pygame
import random

class basic_enemy:
    def __init__(self, X, Y, move):
        self.enemy_image = pygame.image.load("enemy.png")
        self.hp = 10
        self.score = 10
        self.X_deltaval_speed = 0.8
        self.Y_deltaval_speed = 100
        self.X = X
        self.Y = Y
        self.move = move
        self.dead = False
        

class basic_enemy2:
    def __init__(self):
        self.enemy_image = pygame.image.load("cat.png")
        self.hp = 15
        self.score = 15
        self.X_deltaval_speed = 1
        self.X1 = 100
        self.X2 = 1200
        self.Y1 = 100
        self.Y2 = 200
        self.X = 0
        self.Y = 0
        
