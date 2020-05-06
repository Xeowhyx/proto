#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from Game_Player import*
from Game_Enemy import*
from pygame.locals import *


#===========================================================
#  Initialisation
#===========================================================

pygame.init()

                  

fenetre = pygame.display.set_mode((640, 480)    )

Background = pygame.image.load("assets/Background001.png").convert_alpha()
x_b = -1920 - 880
fenetre.blit(Background,(x_b,0))

Ground = pygame.image.load("assets/Ground001.png").convert_alpha()
fenetre.blit(Ground,(-64,0))

Layout = pygame.image.load("assets/Hud_Layout.png").convert_alpha()
fenetre.blit(Layout,(0,0))

perso = pygame.image.load("assets/Dogma_Right.png").convert()
position_perso = (640,320)
#position_perso = perso.get_rect()
fenetre.blit(perso,(position_perso))


#temp = pygame.time.Clock()
#temp=pygame.time. get_ticks ( ) 


#Background = pygame.image.load("Background001.png").convert()
#fenetre.blit(Background,(0,0))


pygame.mixer.music.load("assets/Black Wings.ogg")
pygame.mixer.music.play()
son_jump = pygame.mixer.Sound("assets/Dogma_Attack03.ogg")
son_dash = pygame.mixer.Sound("assets/Dash.ogg")

pygame.display.flip()

continuer = 1

Jumping = False
Son = False
Accroupi = False
Dash_Right = 0
Dash_Left = 0
Time = 0
IA1 = 60
No_Dash = False

vit=1.3

Game_Player = Player(vit,"Droite")
PoliceA = Enemy(250,255,10,0.2,"Gauche","assets/nam police.png",44,65)
PoliceB = Enemy(350,255,10,0.2,"Gauche","assets/nam police.png",44,65)

#Background_Level = Sprite(0,0,2)

#Background_Sprite.move(1)

#===========================================================
#  Boucle du Jeu
#===========================================================
#===========================================================
#  Boucle du Jeu
#===========================================================
#===========================================================
#  Boucle du Jeu
#===========================================================

pygame.key.set_repeat(10,10)
compteur=1


while continuer:
    temp=pygame.time.get_ticks()
   # print(temp)
    
    

    if temp<4000*compteur:  #1sec
        PoliceA.move(PoliceA.direction)
        PoliceB.move(PoliceB.direction)
        
    else:
        compteur+=1
        PoliceA.regard(Game_Player.x,Game_Player.y)
        PoliceB.regard(Game_Player.x,Game_Player.y)
        
        
        
        
    

    #===========================================================
    #  IA
    #===========================================================

    #if IA1 < 180:
     #   IA1 += 1
      #  PoliceA.move(PoliceA.direction)
    #else:
  #      IA1 = 0
 #       PoliceA.regard(Game_Player.x,Game_Player.y)
#        PoliceB.regard(Game_Player.x,Game_Player.y)

    #===========================================================
    #  IA
    #===========================================================

    if Game_Player.y < 270:
        Game_Player.move("Bas")
    else:
        Game_Player.jump_height = 0
        Jumping = False
        Son = False
        Game_Player.poids = 0.2
        

    if Dash_Right >= 1:
        if Time <= 120:
            Time += 1
        else:
            Time = 0
            Dash_Right = 0
            Dash_Left = 0
            Game_Player.speed = vit

    K_press = pygame.key.get_pressed()

#===========================================================
#  Saut
#=========================================================== 

    for event in pygame.event.get():   
        if event.type == QUIT:    
            pygame.quit()
            continuer = 0
            
        if event.type == KEYDOWN:
            if event.key==K_ESCAPE:
                pygame.quit()
                
            elif event.key == K_UP and Jumping == False:
                if Son == False:
                    son_jump.play()
                    Son = True
                Game_Player.jump()

        elif event.type == KEYUP and event.key == K_UP:
            Jumping = True
            Game_Player.poids = 1

#===========================================================
#  Déplacement (Droite)
#=========================================================== 
                
    if K_press[K_RIGHT] and Accroupi == False and event.type == KEYDOWN:
        if Dash_Left >= 3:
            Time = 181
            Dash_Right = 0
            Game_Player.speed = vit
        Dash_Left = 0
        if Game_Player.y >= 270:
            if Dash_Right == 3:
                Game_Player.character = "assets/Dogma_Right_Dash2.png"
            else:
                Game_Player.character = "assets/Dogma_Right.png"
        if Dash_Right >= 2:
            if Dash_Right == 2 and Dash_Left == 0:
                son_dash.play()
            Game_Player.speed = 8
            Time = 0
            Dash_Right = 3
        else:
            if Dash_Right == 0:
                Dash_Right = 1
        Game_Player.move("Droite")
        

    if K_press[K_RIGHT] and Accroupi == False and event.type == KEYUP:
        if Dash_Right == 1:
            Dash_Right = 2     
        else:
            Time = 181
            Game_Player.character = "assets/Dogma_Right.png"
            Dash_Right = 0

    Game_Player.speed = vit
#===========================================================
#  Déplacement (Gauche)
#===========================================================    

    if K_press[K_LEFT] and Accroupi == False and event.type == KEYDOWN:
        if Dash_Right >= 3:
            Time = 181
            Dash_Left = 0
            Game_Player.speed = vit
        Dash_Right = 0
        if Game_Player.y >= 270:
            if Dash_Left == 3:
                Game_Player.character = "assets/Dogma_Left_Dash.png"
            else:
                Game_Player.character = "assets/Dogma_Left.png"
        if Dash_Left >= 2:
            if Dash_Left == 2 and Dash_Right == 0:
                son_dash.play()
            Game_Player.speed = 8
            Time = 0
            Dash_Left = 3
        else:
            if Dash_Left == 0:
                Dash_Left = 1
        Game_Player.move("Gauche")

    if K_press[K_LEFT] and Accroupi == False and event.type == KEYUP:
        if Dash_Left == 1:
            Dash_Left = 2     
        else:
            Time = 181
            Game_Player.character = "assets/Dogma_Left.png"
            Dash_Left = 0

#===========================================================
#  Accroupi
#===========================================================  

    if K_press[K_DOWN] and event.type == KEYDOWN:
        Accroupi = True
        if Game_Player.y >= 270:
            if Game_Player.direction == "Droite":
                Game_Player.character = "assets/Dogma_Right_Down.png"
            if Game_Player.direction == "Gauche":
                Game_Player.character = "assets/Dogma_Left_Down.png"
                
    if not K_press[K_DOWN] and Accroupi == True: #event.type == KEYUP:
        Accroupi = False
        if Game_Player.y >= 270:
            if Game_Player.direction == "Droite":
                Game_Player.character = "assets/Dogma_Right.png"
            if Game_Player.direction == "Gauche":
                Game_Player.character = "assets/Dogma_Left.png"

#===========================================================
#  Défilement de l'écran
#===========================================================        

    if x_b >= -2100 and x_b <= -700:
        x_b += 0.8
    elif x_b >= -1700 and x_b <= -1100:
        x_b += 0.4
    else:
        x_b += 1
    if x_b >= 0:
        x_b = -1920 - 880

#===========================================================
#  Refresh de l'écran
#===========================================================

    def refresh(Policier):
        Enemy = pygame.image.load(Policier.image).convert_alpha()
        fenetre.blit(Enemy,(Policier.x,Policier.y))

    #print(temp)

    
    fenetre.blit(Background, (x_b, 0))
    fenetre.blit(Ground, (-64, 0))
    fenetre.blit(Layout,(0,0))
    
    perso = pygame.image.load(Game_Player.character).convert_alpha()
    fenetre.blit(perso, (Game_Player.x, Game_Player.y))
    refresh(PoliceA)
    refresh(PoliceB)

    pygame.display.flip()

#===========================================================
#  Boucle du Jeu
#===========================================================
#===========================================================
#  Boucle du Jeu
#===========================================================
#===========================================================
#  Boucle du Jeu
#===========================================================

