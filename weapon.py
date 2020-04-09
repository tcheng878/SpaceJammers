import pygame
import random

class basic_bullet:
    def __init__(self, bulletX = 0, bulletY = 0):
        self.name = "Pea Shooter"
        self.bullet_image = pygame.image.load("bullet.png")
        self.damage = 10
        self.bulletX = bulletX + 16
        self.bulletY = bulletY
        self. bullet_X_deltaval_speed = 0 #Basic bullets should only move straight fowards
        self.bullet_Y_deltaval_speed = 5
        self.bullet_state = "ready" #ready/fire

class laser:
    def __init__(self, bulletX = 0, bulletY = 0):
        self.name = "LASER"
        self.bullet_image = pygame.image.load("laser.png")
        self.damage = 1
        self.bullet_state = "ready" #ready/fire