import pygame
from pygame.locals import *


class Enemy:

    def __init__(self,x,y,vie,speed,direction,image,hitbox_x,hitbox_y):
        self.x = x
        self.y = y
        self.vie = vie
        self.speed = speed
        self.direction = direction
        self.image = image
        self.hitbox_x = hitbox_x
        self.hitbox_y = hitbox_y


    def regard(self,x,y):
        if self.x > x:
            self.direction = "Gauche"
            self.image = "assets/nam police_left.png"
        if self.x < x:
            self.direction = "Droite"
            self.image = "assets/nam police_right.png"

    def move(self,direction):
        if self.direction == "Gauche":
            self.x -= self.speed
        if self.direction == "Droite":
            self.x += self.speed
