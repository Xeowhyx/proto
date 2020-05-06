#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame
from pygame.locals import *

class Player:
        
        def __init__(self,speed,direction):
                self.speed = speed
                self.direction = direction
                self.x = 100
                self.y = 270
                self.jump_height = 0
                self.Jump = False
                self.poids = 0.2
                self.character = "assets/Dogma_Right.png"
	   
        def move(self,direction):
                
                if direction == "Droite":
                        self.direction = "Droite"
                        if self.x < 550:
                                self.x += self.speed
                if direction == "Gauche":
                        self.direction = "Gauche"
                        if self.x > 60:
                                self.x -= self.speed
                if direction == "Bas":
                        if self.y < 270:
                                self.y += self.poids
                if direction == "Haut":
                        if self.y > 270:
                                self.y -= self.speed

        def jump(self):         
                if self.jump_height < 120:
                        if self.direction == "Droite":
                                self.character = "assets/Dogma_Right_Jump.png"
                        elif self.direction == "Gauche":
                                self.character = "assets/Dogma_Left_Jump.png"

                        if self.jump_height < 60:
                                self.y -= 20
                                self.jump_height += 16
                        elif self.jump_height < 90:
                                self.y -= 10
                                self.jump_height += 8
                        elif self.jump_height < 120:
                                self.y -= 5
                                self.jump_height += 4

                else:
                        if self.direction == "Droite":
                                self.character = "assets/Dogma_Right_Down.png"
                        if self.direction == "Gauche":
                                self.character = "assets/Dogma_Left_Down.png"
